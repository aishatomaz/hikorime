from typing import Dict, List, Optional, Tuple

import sqlite3
from hikorime.repository.config import DATABASE_PATH, SCHEMA_PATH


class RepositoryConnection:
    """
    Classe para conecao com o repositorio do sqlite3.
    """

    def __init__(self, db_path=DATABASE_PATH):
        self.db_path = db_path  # caminho do database
        self._init_db()

    def _init_db(self):  # Verifica se as tables foram criadas
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            sql = f.read()

        connect = sqlite3.connect(self.db_path)
        connect.executescript(sql)
        connect.commit()

    def _connect(
        self,
    ):  # Isso tambem serve para fechar o repositorio, entao nao preciso usar o finally
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Vou poder usar dicionarios e tuplas com isso
        return conn

    def save(self, query: str, params: Tuple | dict = ()) -> int | None:
        """
        Funcao de criar novas entradas na tabela.

        SqlType:
            INSERT

        Args:
            query: Query sql pura.
            params: Parametros da query em tupla ou dict.

        Returns:
            Retorna o id do que foi criado (se tiver erro, retorna None.)
        """

        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid

    def get_one(self, query: str, params: Tuple | dict = ()) -> Optional[Dict]:
        """
        Funcao de retirar apenas uma entradas da tabela.

        SqlType:
            GET

        Args:
            query: Query sql pura.
            params: Parametros da query em tupla ou dict.

        Returns:
            registro afetado
        """

        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            row = cursor.fetchone()
            return dict(row) if row else None

    def get_many(self, query: str, params: Tuple | dict = ()) -> List[Dict]:
        """
        Funcao de retirar varias entradas da tabela (Inclusive get_all).

        SqlType:
            GET

        Args:
            query: Query sql pura.
            params: Parametros da query em tupla ou dict.

        Returns:
            Registros afetados
        """

        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def update(self, query: str, params: Tuple | dict = ()) -> int:
        """
        Funcao que modifica parametros de linhas da tabela.

        SqlType:
            UPDATE(PUT), LIKE

        Args:
            query: Query sql pura.
            params: Parametros da query em tupla ou dict.

        Returns:
            quantidade de linhas afetadas.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount

    def delete(self, query: str, params: Tuple | dict = ()) -> int:
        """
        Funcao que deleta uma linha da tabela.

        SqlType:
            DELETE

        Args:
            query: Query sql pura.
            params: Parametros da query em tupla ou dict.
        Returns:
            Quantidade de Linhas afetadas
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount
