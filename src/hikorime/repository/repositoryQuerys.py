from hikorime.repository.repositoryConnection import RepositoryConnection

class repositoryQuerys():

    # TODO Fazer querys para hikorime
    
    def __init__(self, table_name: str):
        self.table_name = table_name

    def save(self):
        pass # TODO
        
    def getAll(self, table_name: str):
        """
        debug only, retorna tudo da table
        """

        if not table_name.isidentifier():
            raise ValueError(f"Nome da tabela '{table_name}' nao encontrado")

        query = f"select * from {table_name};"

        return RepositoryConnection().query(query)
    
    def getById(self, id: int):
        data = ({"id": id})

        query = f"select * from {self.table_name} where id = :id;"

        return RepositoryConnection().query(query, data)
    
    def getByColumnName(self, column_name:str, value:str):
        """
            Retorna uma query com o nome (o nome deve dar match exato) e seus valores
        """

        if not column_name.isidentifier():
            raise ValueError(f"Invalid column name: {column_name}")

        data = {"value": value}

        query = f"""SELECT * FROM {self.table_name} WHERE {column_name} = :value;"""

        return RepositoryConnection().query(query, data)
    
    def getLikeByColumnName(self, column_name: str, value: str):
        """
            Retorna uma query com o nome (o nome pode ser parcial) e seus valores
        """

        if not column_name.isidentifier():
            raise ValueError(f"Invalid column name: {column_name}")

        data = {"value": f"%{value}%"} # I like the like operation (:

        query = f"""SELECT * FROM {self.table_name} WHERE {column_name} LIKE :value;"""

        return RepositoryConnection().query(query, data)


    def deleteById(self, id:int):
        data = ({"id": id})

        query = f"DELETE FROM {self.table_name} WHERE id=:id;"

        return RepositoryConnection().query(query, data)
    
    def getQuantityOfRown(self):
        query = f"SELECT COUNT(id) FROM {self.table_name};"

        return RepositoryConnection().query(query)

    # TODO fazer uma descricao melhor
    def putInTable(self, id: int, data: dict):
        """
            Um put, vai apenas mudar uma coluna da linha da tabela
        """
        queries = []
        params = []

        for key, value in data.items():
            if value is None:
                continue

            queries.append(f"UPDATE {self.table_name} SET {key} = :value WHERE id = :id")
            params.append({"id": id, "value": value})

        for query, param in zip(queries, params):
            RepositoryConnection.query(query, param)
