from hikorime.repository.repository_connection import RepositoryConnection
from hikorime.repository.repository_querys import RepositoryQuerys
from datetime import datetime


class RepositoryBagagem(RepositoryQuerys):
    """Repositório para gerenciar bagagens no banco de dados."""

    def __init__(self, table_name: str):
        self.conn = RepositoryConnection()
        self.table_name = table_name

    def get_quantidade_bagagem_by_passageiro(self, passageiro_id: int):
        """Obtém a quantidade total de bagagens de um passageiro."""
        data = {"id": passageiro_id}

        query = f"""
            SELECT COUNT(*) as quantidade 
            FROM {self.table_name} 
            WHERE id_passageiro = :id
        """

        return self.conn.get_one(query, data)

    def get_bagagem_by_date(self, passageiro_id: int, date: datetime):
        """Obtém bagagens de um passageiro por data."""
        data = {"passageiro_id": passageiro_id, "date": date}

        query = f"""
            SELECT * 
            FROM {self.table_name} 
            WHERE id_passageiro = :passageiro_id 
            AND DATE(data_criacao) = DATE(:date)
        """

        return self.conn.get_many(query, data)

    def get_bagagens_by_passageiro(self, passageiro_id: int):
        """Obtém todas as bagagens de um passageiro."""
        data = {"passageiro_id": passageiro_id}

        query = f"""
            SELECT 
                id_bagagem,
                id_passageiro,
                tipo_bagagem,
                peso,
                valor_bagagem,
                data_criacao
            FROM {self.table_name}
            WHERE id_passageiro = :passageiro_id
            ORDER BY data_criacao DESC
        """

        return self.conn.get_many(query, data)

    def salvar_bagagem(self, passageiro_id: int, tipo_bagagem: str, 
                      peso: float, valor_bagagem: float):
        """Salva uma bagagem no banco de dados."""
        query = f"""
            INSERT INTO {self.table_name} 
            (id_passageiro, tipo_bagagem, peso, valor_bagagem)
            VALUES (:passageiro_id, :tipo_bagagem, :peso, :valor_bagagem)
        """

        data = {
            "passageiro_id": passageiro_id,
            "tipo_bagagem": tipo_bagagem,
            "peso": peso,
            "valor_bagagem": valor_bagagem
        }

        return self.conn.save(query, data)