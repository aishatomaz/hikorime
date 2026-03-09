from typing import Dict
from fastapi.exceptions import HTTPException
from datetime import datetime, date, timedelta
from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
from hikorime.repository.repository_compra import RepositoryCompra
from hikorime.models.basemodels.bm_passagem import Passagem
from hikorime.models.basemodels.bm_compra import Compra
from hikorime.models.basemodels.bm_cupom import Cupom
from hikorime.models.enums.status_cupom import StatusCupom


class CompraService(BaseService):
    """Classe que gerencia as operações de compra, incluindo validações de cupons,
    cálculo de bagagem, histórico de compras e criação de cupons."""

    VALOR_MINIMO_COMPRA = 250.0  # Valor mínimo de compra para aplicar desconto

    def __init__(self):
        self.service = RepositoryCompra(table_name="compras", id_column="id_compra")

    def finalizar_compra(self, compra: Compra):
        """
        Finaliza a compra, aplicando desconto se houver cupom e validando o valor mínimo.
        """
        try:
            # Validação de valor mínimo para desconto
            if compra.id_cupom and compra.valor_pago < 250.0:
                raise HTTPException(
                    status_code=400,
                    detail="O valor mínimo para aplicar desconto é de R$ 250,00.",
                )

            # Criar a compra
            id_compra = self.save(compra)

            # Se usou cupom, marcar como indisponível
            if compra.id_cupom:
                self.service.marcar_cupom_como_usado(compra.id_cupom)

            # Verificar se o usuário ganhou um novo cupom (a cada 3 compras)
            total_compras = self.service.count_compras_passageiro(compra.id_passageiro)
            if total_compras > 0 and total_compras % 3 == 0:
                self.cupom_fidelidade(compra.id_passageiro)

            return id_compra
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=400, detail=f"Erro ao finalizar a compra: {str(e)}"
            )

    def cupom_fidelidade(self, id_passageiro: int):
        """
        Gera um cupom de 10% de desconto para o user após 3 compras
        """

        repo_cupom = RepositoryQuerys("cupons")
        novo_cupom = Cupom(
            id_passageiro=id_passageiro,
            percentual_desconto=0.10,
            validade=date.today() + timedelta(days=30),
            status=StatusCupom.DISPONIVEL,
        )

        dados_cupom: dict = novo_cupom.model_dump(exclude={"id_cupom"})
        dados_cupom["status"] = dados_cupom["status"].value

        repo_cupom.save(**dados_cupom)

    def create_compra_passagem(self, passagem: dict):
        """Cria uma nova passagem para compra."""
        try:
            compra_passagem = Passagem(**passagem)
            return self.save(compra_passagem)
        except Exception as e:
            raise HTTPException(
                status_code=400, detail=f"Erro ao criar a passagem: {str(e)}"
            )

    def verificar_passageiro_apto_aplicar_cupom(self, passageiro_id: int) -> bool:
        """Verifica se o passageiro possui cupons válidos e não utilizados.

        Args:
            passageiro_id (int): ID do passageiro a ser verificado.

        Returns:
            bool: True se o passageiro possui cupons válidos, False caso contrário.
        """
        cupom = self.service.get_valid_cupom_by_passageiro(passageiro_id)
        return bool(cupom)

    def calcular_valor_bagagem(self, peso: float) -> float:
        """Calcula o valor da bagagem baseado no peso.

        Fórmula: VALOR_FIXO + (peso * TAXA_VARIAVEL)
        - VALOR_FIXO: R$ 50,00
        - TAXA_VARIAVEL: R$ 5,00 por kg

        Args:
            peso (float): Peso da bagagem em kg.

        Returns:
            float: Valor calculado da bagagem.

        Raises:
            ValueError: Se o peso for inválido ou exceder o limite máximo.
        """
        try:
            peso = float(peso)
            if peso <= 0:
                raise ValueError("O peso deve ser maior que zero")
            if peso > 10:
                raise ValueError("O peso máximo permitido é 10 kg")

            return self.service.calcular_valor_bagagem(peso)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_valor_bagagens_by_passageiro_id(self, passageiro_id: int):
        """Recupera todas as bagagens associadas a um passageiro.

        Args:
            passageiro_id (int): ID do passageiro.

        Returns:
            List[Dict]: Lista de dicionários representando as bagagens do passageiro.
        """
        return self.service.get_valor_bagagens_by_passageiro_id(passageiro_id)

    def calcular_valores(
        self, passageiro_id: int, cupom_id: int | None = None
    ) -> Dict[str, float | bool]:
        """Calcula o valor total da compra de um passageiro.

        A função soma o valor da última passagem adquirida pelo passageiro
        com o valor das bagagens (quando disponível) e aplica o desconto de cupom,
        caso o passageiro seja elegível e o valor mínimo seja atingido.

        Args:
            passageiro_id (int): ID do passageiro para o qual o total será calculado.
            cupom_id: ID do cupom a ser aplicado.

        Returns:
            dict: Dicionário contendo:
                - valor_passagem: Valor da passagem
                - valor_bagagem: Valor total das bagagens
                - valor_subtotal: Soma de passagem + bagagem
                - valor_desconto: Valor do desconto aplicado
                - valor_total: Valor final após desconto
                - cupom_aplicado: Se um cupom foi aplicado
        Raises:
            RuntimeError: Se o passageiro não possui passagens cadastradas.
        """

        # Returns:
        #     dict: Dicionário contendo:
        #         - valor_passagem: Valor da passagem
        #         - valor_bagagem: Valor total das bagagens
        #         - valor_subtotal: Soma de passagem + bagagem
        #         - valor_desconto: Valor do desconto aplicado
        #         - valor_total: Valor final após desconto
        #         - cupom_aplicado: Se um cupom foi aplicado

        # Obter as passagens do passageiro
        passagens = self.service.get_passagens_by_passageiro(passageiro_id)

        if not passagens:
            raise RuntimeError("Passageiro não tem passagens cadastradas")

        # Pega o valor da última passagem
        ultima_passagem = passagens[0]
        valor_passagem = float(
            ultima_passagem.get(
                "valor_pago", ultima_passagem.get("valor_base_passagem", 0)
            )
        )

        # Obter o valor das bagagens, se houver
        bagagens = self.service.get_valor_bagagens_by_passageiro_id(passageiro_id)
        valor_bagagem = sum(float(b.get("valor_bagagem", 0)) for b in bagagens)

        # Calcular subtotal
        valor_subtotal = valor_passagem + valor_bagagem

        # Inicializar variáveis de desconto
        valor_desconto = 0.0
        cupom_aplicado = False

        # Verificar se o valor mínimo foi atingido e se há cupom disponível
        if valor_subtotal >= self.VALOR_MINIMO_COMPRA:
            if cupom_id is not None:
                cupom = self.service.get_valid_cupom_by_passageiro(passageiro_id)
                if cupom and cupom.get("id_cupom") == cupom_id:
                    desconto_percentual = float(cupom.get("percentual_desconto", 0))
                    valor_desconto = valor_subtotal * desconto_percentual
                    cupom_aplicado = True
            elif self.verificar_passageiro_apto_aplicar_cupom(passageiro_id):
                cupom = self.service.get_valid_cupom_by_passageiro(passageiro_id)
                if cupom:
                    desconto_percentual = float(cupom.get("percentual_desconto", 0))
                    valor_desconto = valor_subtotal * desconto_percentual
                    cupom_aplicado = True

        valor_total = valor_subtotal - valor_desconto

        return {
            "valor_passagem": round(valor_passagem, 2),
            "valor_bagagem": round(valor_bagagem, 2),
            "valor_subtotal": round(valor_subtotal, 2),
            "valor_desconto": round(valor_desconto, 2),
            "valor_total": round(valor_total, 2),
            "cupom_aplicado": cupom_aplicado,
        }

    def get_compras_by_id(self, passageiro_id: int):
        """Retorna o histórico de compras de um passageiro."""
        return self.service.get_compras(passageiro_id)

    def get_valid_cupom_by_passageiro_id(self, passageiro_id: int):
        """Retorna o cupom válido disponível para o passageiro."""
        return self.service.get_valid_cupom_by_passageiro(passageiro_id)

    def get_cupons_by_passageiro_id(self, passageiro_id: int):
        """Retorna todos os cupons do passageiro com seus status."""
        return self.service.get_cupons_by_passageiro(passageiro_id)

    def get_passagens_by_passageiro_id(self, passageiro_id: int):
        """Retorna todas as passagens do passageiro."""
        return self.service.get_passagens_by_passageiro(passageiro_id)

    def get_tickets_disponiveis(self, local_origem: str, local_destino: str):
        """Busca passagens (tickets) disponíveis com filtros opcionais.

        Args:
            local_origem (str, optional): Cidade/local de origem.
            local_destino (str, optional): Cidade/local de destino.

        Returns:
            List[Dict]: Lista de voos disponíveis com informações de assentos.
        """
        return self.service.get_tickets_disponiveis(local_origem, local_destino)

    def criar_cupom_manual(
        self, passageiro_id: int, percentual_desconto: float, dias_validade: int = 30
    ) -> dict:
        """Cria um cupom manualmente para um passageiro.

        Args:
            passageiro_id (int): ID do passageiro que receberá o cupom.
            percentual_desconto (float): Percentual de desconto (ex: 0.1 para 10%).
            dias_validade (int): Número de dias até a validade do cupom (padrão: 30).

        Returns:
            dict: Informações do cupom criado.

        Raises:
            HTTPException: Se houver erro na criação do cupom.
        """
        try:
            # Validar percentual de desconto
            if not isinstance(percentual_desconto, (int, float)):
                raise ValueError("O percentual de desconto deve ser numérico")

            if percentual_desconto < 0 or percentual_desconto > 1:
                raise ValueError(
                    "O percentual de desconto deve estar entre 0 e 1 (0% a 100%)"
                )

            # Calcular data de validade
            data_validade = date.today() + timedelta(days=dias_validade)

            # Criar o cupom
            cupom_id = self.service.criar_cupom(
                passageiro_id, percentual_desconto, data_validade
            )

            return {
                "id_cupom": cupom_id,
                "id_passageiro": passageiro_id,
                "percentual_desconto": percentual_desconto,
                "validade": str(data_validade),
                "status": "DISPONIVEL",
                "usado": False,
                "mensagem": "Cupom criado com sucesso",
            }
        except Exception as e:
            raise HTTPException(
                status_code=400, detail=f"Erro ao criar cupom: {str(e)}"
            )

    def aplicar_cupom_na_compra(
        self, passageiro_id: int, cupom_id: int, valor_compra: float
    ) -> dict:
        """Aplica um cupom em uma compra e marca como utilizado.

        Args:
            passageiro_id (int): ID do passageiro.
            cupom_id (int): ID do cupom a ser aplicado.
            valor_compra (float): Valor da compra para validação do mínimo.

        Returns:
            dict: Informações da aplicação do cupom.

        Raises:
            HTTPException: Se o cupom não for válido ou já foi utilizado.
        """
        try:
            # Validar valor mínimo
            if valor_compra < self.VALOR_MINIMO_COMPRA:
                raise ValueError(
                    f"Valor mínimo de compra é R$ {self.VALOR_MINIMO_COMPRA:.2f}. "
                    f"Valor atual: R$ {valor_compra:.2f}"
                )

            # Buscar cupom
            cupom = self.service.get_valid_cupom_by_passageiro(passageiro_id)

            if not cupom:
                raise ValueError("Nenhum cupom válido encontrado para este passageiro")

            if cupom.get("id_cupom") != cupom_id:
                raise ValueError("Cupom não pertence a este passageiro ou não é válido")

            # Calcular desconto
            desconto_percentual = float(cupom.get("percentual_desconto", 0))
            valor_desconto = valor_compra * desconto_percentual
            valor_final = valor_compra - valor_desconto

            # Marcar cupom como usado
            self.service.marcar_cupom_como_usado(cupom_id)

            return {
                "cupom_id": cupom_id,
                "percentual_desconto": desconto_percentual,
                "valor_original": round(valor_compra, 2),
                "valor_desconto": round(valor_desconto, 2),
                "valor_final": round(valor_final, 2),
                "mensagem": "Cupom aplicado com sucesso",
            }
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(
                status_code=400, detail=f"Erro ao aplicar cupom: {str(e)}"
            )

    def salvar_compra(self, compra_data: dict) -> int:
        """Salva uma compra no banco de dados.

        Args:
            compra_data (dict): Dicionário com os dados da compra.

        Returns:
            int: ID da compra criada.
        """
        try:
            return self.service.salvar_compra(compra_data)
        except Exception as e:
            raise HTTPException(
                status_code=400, detail=f"Erro ao salvar compra: {str(e)}"
            )
