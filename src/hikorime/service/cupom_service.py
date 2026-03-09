from fastapi import HTTPException
from datetime import date, timedelta
from hikorime.models.basemodels.bm_cupom import Cupom
from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
from hikorime.repository.repository_compra import RepositoryCompra


class CupomService(BaseService):
    """Serviço para gerenciar cupons de desconto dos passageiros."""

    def __init__(self):
        self.repo = RepositoryQuerys("cupons")
        self.compra_repo = RepositoryCompra("compras")

    def create_cupom(self, cupom_data: dict):
        """Cria um novo cupom.

        Args:
            cupom_data (dict): Dicionário com os dados do cupom a ser salvo.
                Deve conter: percentual_desconto, validade, status

        Returns:
            dict: Dados do cupom salvo (id gerado, etc.)
            
        Raises:
            HTTPException: Se houver erro na criação do cupom.
        """
        try:
            cupom = Cupom(**cupom_data)
            return self.save(cupom)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao criar cupom: {str(e)}")

    def criar_cupom_para_passageiro(self, passageiro_id: int, percentual_desconto: float,
        dias_validade: int = 30) -> dict:
        """Cria um cupom para um passageiro específico.

        Args:
            passageiro_id (int): ID do passageiro que receberá o cupom.
            percentual_desconto (float): Percentual de desconto (0 a 1).
            dias_validade (int): Número de dias até a validade (padrão: 30).

        Returns:
            dict: Informações do cupom criado.
            
        Raises:
            HTTPException: Se houver erro na criação.
        """
        try:
            # Validar percentual
            if not isinstance(percentual_desconto, (int, float)):
                raise TypeError("Percentual deve ser numérico")
            
            if percentual_desconto < 0 or percentual_desconto > 1:
                raise ValueError("Percentual deve estar entre 0 e 1")
            
            # Calcular validade
            data_validade = date.today() + timedelta(days=dias_validade)
            
            # Criar cupom
            cupom_id = self.compra_repo.criar_cupom(
                passageiro_id,
                percentual_desconto,
                data_validade
            )
            
            return {
                "id_cupom": cupom_id,
                "id_passageiro": passageiro_id,
                "percentual_desconto": percentual_desconto,
                "validade": str(data_validade),
                "status": "DISPONIVEL",
                "usado": False
            }
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao criar cupom: {str(e)}")

    def obter_cupons_passageiro(self, passageiro_id: int) -> list[dict]:
        """Obtém todos os cupons de um passageiro.

        Args:
            passageiro_id (int): ID do passageiro.

        Returns:
            list: Lista de cupons do passageiro.
        """
        return self.compra_repo.get_cupons_by_passageiro(passageiro_id)

    def obter_cupom_valido(self, passageiro_id: int) -> dict:
        """Obtém o primeiro cupom válido e não utilizado do passageiro.

        Args:
            passageiro_id (int): ID do passageiro.

        Returns:
            dict: Dados do cupom válido ou None.
        """
        return self.compra_repo.get_valid_cupom_by_passageiro(passageiro_id)

    def marcar_cupom_como_usado(self, cupom_id: int) -> int:
        """Marca um cupom como utilizado.

        Args:
            cupom_id (int): ID do cupom.

        Returns:
            int: Número de linhas afetadas.
        """
        return self.compra_repo.marcar_cupom_como_usado(cupom_id)

    def verificar_cupom_valido(self, cupom_id: int, passageiro_id: int) -> bool:
        """Verifica se um cupom é válido para um passageiro.

        Args:
            cupom_id (int): ID do cupom.
            passageiro_id (int): ID do passageiro.

        Returns:
            bool: True se o cupom é válido, False caso contrário.
        """
        cupom = self.compra_repo.get_valid_cupom_by_passageiro(passageiro_id)
        
        if not cupom:
            return False
        
        return cupom.get("id_cupom") == cupom_id