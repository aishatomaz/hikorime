from typing import Any

from hikorime.repository.repository_connection import RepositoryConnection


class RepositoryQuerys:
    """
    Guarda as querys base para outro repositorios, e services
    """

    def __init__(self, table_name: str):
        self.table_name = table_name

    def save(self, **kwargs: Any):
        """
        Salva os dados dentro do banco de dados(metodo POST)

        Args:
            kwargs: qualquer elemento a ser salvo(
            os argumentos tem que bater junto ao da classe modelo)

        Returns:
            dict[str, Any]: um dicionario a ser salvo no banco de dados
        """

        if not self.table_name.isidentifier():
            raise ValueError(f"Nome da tabela inválido: {self.table_name}")

        if not kwargs:
            raise ValueError("Nenhum dado fornecido para salvar")

        # Valida os nomes das colunas
        for column in kwargs.keys():
            if not column.isidentifier():
                raise ValueError(f"Nome de coluna inválido: {column}")

        columns = ", ".join(kwargs.keys())
        placeholders = ", ".join(
            f":{key}" for key in kwargs.keys()
        )  # Isso foi horrivel de achar, basicamente faz um loop entre cada par de tupla

        query = f"""
            INSERT INTO {self.table_name} ({columns})
            VALUES ({placeholders});
        """

        return RepositoryConnection().save(query, kwargs)

    def get_all(self):
        """
        Pega todos as entidades da tabela.

        Returns:
            dict: um dicionario representando todas as entidades da tabela.
        """

        if not self.table_name.isidentifier():
            raise ValueError(f"Nome da tabela '{self.table_name}' nao encontrado")

        query = f"select * from {self.table_name};"

        return RepositoryConnection().get_many(query)

    def get_by_id(self, id: int):
        """
        Pega uma entidade da tabela por seu id.

        Args:
            id: O id da entidade a ser buscada.

        Returns:
            dict | None: Um dicionario representando a entidade encontrada,
            ou None se nenhuma entidade com o id informado existir.
        """
        data = {"id": id}

        query = f"select * from {self.table_name} where id = :id;"

        return RepositoryConnection().get_one(query, data)

    def get_by_column_name(self, column_name: str, value: str):
        """
        Pega todas as entidades, de uma determinada coluna.

        args:
            column_name: nome da coluna a ser buscada.
            value: String do que voce quer buscar (Tem que bater todos os caracteres).

        Returns:
            dict | None: Um dicionario representando a entidade(s) encontrada(s),
            ou None se a coluna nao existir, ou vazio se nao for encontrado valores
            que batam com o que foi pedido.
        """

        if not column_name.isidentifier():
            raise ValueError(f"Nome da coluna invalido: {column_name}")

        data = {"value": value}

        query = f"""SELECT * FROM {self.table_name} WHERE {column_name} = :value;"""

        return RepositoryConnection().get_one(query, data)

    def get_like_by_column_name(self, column_name: str, value: str):
        """
        Pega todas as entidades, de uma determinada coluna.

        args:
            column_name: nome da coluna a ser buscada.
            value: String parcial do que voce precisa buscar.

        Returns:
            dict | None: Um dicionario representando a entidade(s) encontrada(s),
            ou None se a coluna nao existir, ou vazio se nao for encontrado valores
            que batam com o que foi pedido.
        """

        if not column_name.isidentifier():
            raise ValueError(f"Invalid column name: {column_name}")

        # Nao ouse tirar o comentario abaixo
        data = {"value": f"%{value}%"}  # I like the like operation (:

        query = f"""SELECT * FROM {self.table_name} WHERE {column_name} LIKE :value;"""

        return RepositoryConnection().get_one(query, data)

    def delete_by_id(self, id: int):
        """
        Deleta uma entidade usando seu id.

        Args:
            id: O id que sera deletado da tabela.

        Returns:

        """
        data = {"id": id}

        query = f"DELETE FROM {self.table_name} WHERE id=:id;"

        return RepositoryConnection().delete(query, data)

    def get_quantity_of_rown(self):
        """
        so fiz isso para literalmente para saber quantos ids relmente existem na tabela.
        """
        query = f"SELECT COUNT(id) FROM {self.table_name};"

        return RepositoryConnection().get_one(query)

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

            queries.append(
                f"UPDATE {self.table_name} SET {key} = :value WHERE id = :id"
            )
            params.append({"id": id, "value": value})

        for query, param in zip(
            queries, params
        ):  # Isso serve para cada put ser colocado de forma individual.
            RepositoryConnection.update(query, param)
