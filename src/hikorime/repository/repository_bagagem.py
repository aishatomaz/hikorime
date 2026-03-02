from hikorime.repository.repository_connection import RepositoryConnection
from hikorime.repository.repository_querys import RepositoryQuerys
from datetime import datetime


class RepositoryBagagem(RepositoryQuerys):
    def __init__(self, table_name: str):
        self.conn = RepositoryConnection()
        self.table_name = table_name

    def get_quantidade_bagagem_by_passageiro(self, passageiro_id: int):
        data = {"id": passageiro_id}

        query = f"select * from {self.table_name} where passageiro_id = :id;"

        return self.conn.get_one(query, data)

    def get_bagagem_by_date(self, passageiro_id: int, date: datetime):
        data = {"passagero_id": passageiro_id, "date": date}

        query = f"select * from {self.table_name} where passageiro_id = :id AND date = : date;"

        return self.conn.get_many(query, data)
