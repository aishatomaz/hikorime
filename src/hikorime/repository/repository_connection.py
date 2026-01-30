import sqlite3

from hikorime.repository.config import DATABASE_PATH

from typing import Any


class RepositoryConnection:
    """
    Conecta ao banco de dados, e faz querys automaticas.
    """

    def __init__(
        self, db_path=DATABASE_PATH
    ):  # Voce pode sobrescrever a path em testes, path da db em config.py
        self.db_path = db_path  # caminho do database

    def query(
        self, query: str, data: dict[str, Any] | None = None
    ):  # o Any do dicionario, e que as vezes devo usar int para selecionar id po exemplo
        """
        args:
            query: query sql
            data: dados da query (dict ou tupla, default = None)
        """

        # Se nao existir, cria o repositorio automaticamente
        connect = sqlite3.connect(self.db_path)
        connect.row_factory = sqlite3.Row
        cursor = connect.cursor()

        try:
            # Executa Select
            if query.strip().upper().startswith("SELECT"):
                if data is not None:
                    cursor.execute(query, data)
                else:
                    cursor.execute(query)
                print("Dados selecionados com sucesso")
                return cursor.fetchall()

            # Executa 'update', 'insert' e 'delete'
            if data is not None:
                cursor.execute(query, data)
            else:
                cursor.execute(query)

            connect.commit()
            print("Mudancas realizadas com sucesso!")
            return True

        except Exception as error:
            print(f"error - {error} dando rollback")
            connect.rollback()  # GOTO antes da ultima interacao
            return None

        finally:
            cursor.close()
            connect.close()
