from typing import Any, Dict, List

from hikorime.repository.repository_connection import RepositoryConnection


class RepositoryQuerys:
    """
    Guarda as querys base para outro repositorios, e services
    """

    def __init__(self, table_name: str):
        self.table_name = table_name
        self.conn = RepositoryConnection()

    def save(self, **kwargs: Any) -> int:
        """
        Salva os dados dentro do banco de dados(método POST)

        Args:
            kwargs: qualquer elemento a ser salvo(
            os argumentos tem que bater junto ao da classe modelo)

        Returns:
            int: o id da entidade salva
        """

        if not self.table_name.isidentifier():
            raise ValueError(f"Nome da tabela inválido: {self.table_name}")

        if not kwargs:
            raise ValueError("Nenhum dado fornecido para salvar")

        # Valida os nomes das colunas
        for column in kwargs.keys():  # {key: value}
            if not column.isidentifier():
                raise ValueError(f"Nome de coluna inválido: {column}")

        columns = ", ".join(kwargs.keys())
        placeholders = ", ".join(
            f":{key}" for key in kwargs.keys()
        )  # faz um loop entre cada par de tupla

        query = f"""
            INSERT INTO {self.table_name} ({columns})
            VALUES ({placeholders});
        """

        return self.conn.save(query, kwargs)

    def get_all(self) -> List[Dict]:
        """
        Pega todos as entidades da tabela.

        Returns:
            List[dict]: um dicionario representando todas as entidades da tabela.
        """

        if not self.table_name.isidentifier():
            raise ValueError(f"Nome da tabela '{self.table_name}' nao encontrado")

        query = f"select * from {self.table_name};"

        return self.conn.get_many(query)

    def get_by_id(self, entity_id: int, id_column: str) -> dict | None:
        """
        Pega uma entidade da tabela por seu id.

        Args:
            entity_id: O id da entidade a ser buscada.
            id_column: O nome da coluna que o id sera buscado (Geralmente, nome da tabela no singular).

        Returns:
            dict | None: Um dicionario representando a entidade encontrada,
            ou None se nenhuma entidade com o id informado existir.
        """
        data = {"entity_id": entity_id, "id_column": id_column}

        query = f"select * from {self.table_name} where {id_column} = :entity_id;"

        return self.conn.get_one(query, data)

    def get_by_column_name(
        self, column_name: str, value: str | int
    ) -> List[Dict] | None:
        """
        Pega entidade(s), de uma determinada coluna.

        args:
            column_name: nome da coluna a ser buscada.
            value: String do que voce quer buscar (Tem que bater todos os caracteres), ou inteiro se for id por exemplo.

        Returns:
            dict | None: Um dicionario representando a entidade(s) encontrada(s),
            ou None se a coluna nao existir, ou vazio se nao for encontrado valores
            que batam com o que foi pedido.
        """

        if not column_name.isidentifier():
            raise ValueError(f"Nome da coluna invalido: {column_name}")

        data = {"value": value}

        query = f"""SELECT * FROM {self.table_name} WHERE {column_name} = :value;"""

        return self.conn.get_many(query, data)

    def get_like_by_column_name(self, column_name: str, value: str | int):
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

        return self.conn.get_many(query, data)

    def delete_by_id(self, id: int):
        """
        Deleta uma entidade usando seu id.

        Args:
            id: O id que sera deletado da tabela.
        Returns:
            dict | None: um dicionario representando a entidade deletada, ou None, caso nao for encontrada.
        """
        data = {"id": id}

        query = f"DELETE FROM {self.table_name} WHERE id=:id;"

        return self.conn.delete(query, data)

    def get_quantity_of_rown(self):
        """
        Conta a quantiddade total de linhas de uma tabela.

        Returns:
            Um dicionario, contendo a quantidade de  linhas.
        """
        query = f"SELECT COUNT(id) FROM {self.table_name};"

        return self.conn.get_one(query)

    def update_column(self, id: int, data: dict):
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

    def get_table_name(self) -> str:  # Util para debug, e vai ser usado em controller
        """
        Retorna o nome da tabela que esta sendo usado
        """
        return self.table_name

    def get_passageiro_by_usuario(self, id_usuario: int) -> dict:
        query = """
                SELECT *
                FROM passageiros
                WHERE id_usuario = :id_usuario 
                """
        return self.conn.get_one(query, {"id_usuario": id_usuario})

