from hikorime.service.base_service import BaseService
from hikorime.repository.repository_compra import RepositoryCompra


class CompraService(BaseService):
    """Classe salva os valores de Compra no Banco de Dados."""

    def __init__(self):
        # Retirei events, e deixei apenas service. em repoCompra, ele ja pega oque tem em repoQuery.
        self.service = RepositoryCompra("compra")

    def verificar_passageiro_apto_aplicar_cupom(self, passageiro_id: int) -> bool:
        """Verifica se existem cupons válidos para o passageiro, com validade maior que a data atual.

        Args:
            passageiro_id (int): ID do passageiro a ser verificado.

        Returns:
            bool: True se o passageiro possui cupons válidos, False caso contrário.
        """
        # Chama o repositório para verificar cupons válidos para o passageiro
        cupons_validos = self.service.get_valid_cupom_by_passageiro(passageiro_id)

        # Verifica se existem cupons válidos
        return bool(cupons_validos)

    def get_valor_bagagens_by_passageiro_id(self, passageiro_id: int):
        """Recupera todas as bagagens associadas a um passageiro.

        Args:
            passageiro_id (int): ID do passageiro.

        Returns:
            List[Dict]: Lista de dicionários representando as bagagens do passageiro.
        """
        return self.service.get_valor_bagagens_by_passageiro_id(passageiro_id)

    # TODO: trocar para decimal
    def calcular_total(self, passageiro_id: int):
        """Calcula o valor total da compra de um passageiro.

        A função soma o valor da última passagem adquirida pelo passageiro
        com o valor das bagagens (quando disponível) e aplica o desconto de cupom,
        caso o passageiro seja elegível.

        Args:
            passageiro_id (int): ID do passageiro para o qual o total será calculado.

        Returns:
            float: Valor total da compra após somar passagens, bagagens e aplicar desconto do cupom.
                Retorna 0 se o passageiro não possuir passagens registradas.
        """
        # Obter as passagens do passageiro
        passagens = self.service.get_passagens_by_passageiro(passageiro_id)

        if not passagens:
            raise RuntimeError("Passageiro não tem passagens cadastradas")

        # Pega o valor da última passagem
        ultima_passagem = passagens[0]
        valor_total = ultima_passagem["valor_pago"]

        # Obter o valor das bagagens, se houver
        bagagens = self.service.get_valor_bagagens_by_passageiro_id(passageiro_id)
        valor_bagagens = sum(b["valor"] for b in bagagens)

        # Somar o valor das bagagens ao total
        valor_total += valor_bagagens

        # Verificar se o passageiro pode aplicar o cupom de desconto
        if self.verificar_passageiro_apto_aplicar_cupom(passageiro_id):
            cupom = self.service.get_valid_cupom_by_passageiro(passageiro_id)
            if cupom:
                desconto = cupom["desconto"]
                valor_total *= 1 - desconto  # Aplica o desconto

        return round(valor_total, 2)  # Retorna o valor total arredondado
