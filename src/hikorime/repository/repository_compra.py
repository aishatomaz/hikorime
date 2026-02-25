from warnings import deprecated
from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.repository.repository_connection import RepositoryConnection


class RepositoryCompra(RepositoryQuerys):
    """Classe do repositório para eventos específicos ou consultas mais detalhadas. Suas funções serão utilizadas pela camada de Service
    para validar regras de negócio."""

    def __init__(self, table_name: str):
        self.connection = RepositoryConnection()
        self.table_name = table_name

    def verificar_quantidade_compras_passageiro_maior_igual_3(  # Se estou verificando quantas passagens o passageiro tem, porque tenho de passar a quantia de passagens
        self,
        passageiro_id: int,  # passagens_vendidas: int
    ) -> bool:
        """Verifica se existem passageiros com 3 ou mais compras registradas.

        Executa uma query no banco para contar quantas compras cada passageiro realizou
        e retorna True se houver algum passageiro com 3 ou mais compras.

        Returns:
            bool: True se houver passageiros com 3 ou mais compras, False caso contrário.
        """

        # data_old = {"passageiro_id": passageiro_id, "passagens_vendidas": passagens_vendidas}
        data = {"passageiro_id": passageiro_id}

        query = """
        SELECT passagens_vendidas.passageiro_id, COUNT(*) as Total
        FROM passagens_vendidas
        WHERE passagens_vendidas.passageiro_id = :passageiro_id
        GROUP BY passagens_vendidas.passageiro_id
        HAVING COUNT(*) >= 3
        """
        # query_old = f"""SELECT :passageiro_id, COUNT(*) as Total FROM  GROUP BY :passageiro_id HAVING COUNT(*) >= 3"""
        result = self.connection.get_one(query, data)
        return bool(result)

    @deprecated(
        "Mudado para 'verificar_data_cupom_passageiro', para fazer a verificacao correta"
    )
    def verificar_data_validade_maior_que_hoje(
        self,  # passageiro_id: int
    ) -> bool:
        # data = {"passageiro_id": passageiro_id} # Não precisamos do id do passageiro, se a intencao for verificar os cupons
        """Verifica se existem cupons com validade maior que a data atual.

        Executa uma query no banco para buscar cupons válidos.

        Returns:
            bool: True se houver cupons válidos, False caso contrário.
        """
        query = """SELECT validade FROM cupom WHERE validade >= date('now')"""
        result = self.connection.get_many(query)
        return bool(result)

    def get_compras(self, passageiro_id: int):
        """
        Retorna todas as compras realizadas por um passageiro, ordenadas pela data de compra.

        Args:
            passageiro_id (int): O ID do passageiro cujas compras serao recuperadas.

        Returns:
            list[dict]: Lista de dicionarios com as compras do passageiro.
        """

        data = {"passageiro_id": passageiro_id}
        query = """
            SELECT               
                data_compra,
                valor_pago,
                tipo_pagamento
            FROM compra
            WHERE passageiro_id = :passageiro_id
            ORDER BY data_compra DESC
        """
        return RepositoryConnection().get_many(query, data)

    def get_valid_cupom_by_passageiro(self, passageiro_id: int):
        """Retorna cupons válidos para o passageiro."""
        # TODO: Verificar o limite de cupons com a equipe
        sql = """
            SELECT desconto
            FROM cupons
            WHERE passageiro_id = :passageiro_id AND validade >= date('now')
            LIMIT 1
        """
        data = {"passageiro_id": passageiro_id}
        return RepositoryConnection().get_one(sql, data)

    def get_passagens_by_passageiro(self, passageiro_id: int):
        """Retorna todas as passagens associadas ao passageiro."""

        data = {"passageiro_id": passageiro_id}
        sql = """
            SELECT passagem_id
            FROM passagens
            WHERE passageiro_id = :passageiro_id
        """
        return RepositoryConnection().get_many(sql, data)

    def get_valor_bagagens_by_passageiro_id(self, passageiro_id: int):
        """Retorna todas as bagagens associadas ao passageiro."""

        data = {"passageiro_id": passageiro_id}
        sql = """
            SELECT valor
            FROM bagagens
            WHERE passageiro_id = :passageiro_id
        """
        return RepositoryConnection().get_many(sql, data)
