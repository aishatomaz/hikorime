import sqlite3

from typing import Any

from hikorime.repository.config import DATABASE_PATH, SCHEMA_PATH


class RepositoryConnection:
    """
    Conecta ao banco de dados, e faz querys automaticas.
    """

    def __init__(
        self, db_path=DATABASE_PATH
    ):  # Voce pode sobrescrever a path em testes, path da db em config.py
        self.db_path = db_path  # caminho do database
        self._init_db()

    def _init_db(self):  # Verifica se as tables foram criadas
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            sql = f.read()

        connect = sqlite3.connect(self.db_path)
        connect.executescript(sql)
        connect.commit()

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
                rows = cursor.fetchall()
                return [
                    dict(row) for row in rows
                ]  # Converte para dicionario os valores, corrigido o problema de get em registro.service

            # Executa 'update', 'insert' e 'delete'
            if data is not None:
                cursor.execute(query, data)
            else:
                cursor.execute(query)

            connect.commit()
            print("Mudancas realizadas com sucesso!")
            return cursor.rowcount  # Antes estava True

        except Exception as error:
            print(f"error - {error} dando rollback")
            connect.rollback()  # GOTO antes da ultima interacao
            return None

        finally:
            cursor.close()
            connect.close()
