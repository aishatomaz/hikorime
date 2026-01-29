from hikorime.repository.repository_connection import RepositoryConnection

class RepositoryQuerys:

    # TODO Fazer querys para hikorime
    
    def __init__(self, table_name: str):
        self.table_name = table_name

    def save(self):
        pass # TODO # O save depende do que vamos salvar especificamente.
        
    def get_all(self, table_name: str):
        """
        debug only, retorna tudo da tabela
        """

        if not table_name.isidentifier():
            raise ValueError(f"Nome da tabela '{table_name}' nao encontrado")

        query = f"select * from {table_name};"

        return RepositoryConnection().query(query)
    
    def get_by_id(self, id: int):
        data = ({"id": id})

        query = f"select * from {self.table_name} where id = :id;"

        return RepositoryConnection().query(query, data)
    
    def get_by_column_name(self, column_name:str, value:str):
        """
            Retorna uma query usando o nome da coluna
            (Se precisar de um valor parcial, use getLikeByColumnName)
            args:
                column_name: nome da coluna
                value = oque voce quer *exatamente* adequirir
        """

        if not column_name.isidentifier():
            raise ValueError(f"Nome da coluna invalido: {column_name}")

        data = {"value": value}

        query = f"""SELECT * FROM {self.table_name} WHERE {column_name} = :value;"""

        return RepositoryConnection().query(query, data)
    
    def get_like_by_column_name(self, column_name: str, value: str):
        """
            Retorna uma query usando o nome da coluna
            (Se precisar de um valor exatamente como escreveu, use getByColumnName)
            args:
                column_name: nome da coluna
                value = oque voce quer adequirir (Pode ser um nome parcial)
                exemplo:
                value = dhon, ira pegar qualquer valor que contenha os caracteres juntos dhon, ou seja, dhon, dhonatan, dhonatian, etc
        """

        if not column_name.isidentifier():
            raise ValueError(f"Invalid column name: {column_name}")

        data = {"value": f"%{value}%"} # I like the like operation (:

        query = f"""SELECT * FROM {self.table_name} WHERE {column_name} LIKE :value;"""

        return RepositoryConnection().query(query, data)


    def delete_by_id(self, id:int):
        """
            deleta alguma coisa usando seu id
        """
        data = ({"id": id})

        query = f"DELETE FROM {self.table_name} WHERE id=:id;"

        return RepositoryConnection().query(query, data)
    
    def get_quantity_of_rown(self):
        """
            so fiz isso para literalmente para saber quantos ids relmente existem na tabela.
        """
        query = f"SELECT COUNT(id) FROM {self.table_name};"

        return RepositoryConnection().query(query)

    def put_in_table(self, id: int, data: dict):
        """
            Um put, vai apenas mudar uma coluna da linha da tabela
            exemplo, posso mudar 'invers' para 'sudo invers', sem alterar qualquer outro dado dele.
        """
        queries = []
        params = []

        for key, value in data.items():
            if value is None:
                continue

            queries.append(f"UPDATE {self.table_name} SET {key} = :value WHERE id = :id")
            params.append({"id": id, "value": value})

        for query, param in zip(queries, params): # Isso serve para cada put ser colocado de forma individual.
            RepositoryConnection.query(query, param)
