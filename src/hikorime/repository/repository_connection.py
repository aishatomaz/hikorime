from typing import Any, Dict, List, Optional, Tuple

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
        connect.close()

    def _connect(
        self,
    ):  # Serve para criar a conexao com o banco de dados, e ativar as chaves estrangeiras
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  
        conn.row_factory = sqlite3.Row  # pode usar dicionarios e tuplas com isso
        return conn

    def save(self, query: str, params: Tuple | dict = ()) -> int:
        """
        Funcao de criar novas entradas na tabela.
        """
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as error:
            raise ValueError(f"Erro ao executar: {error}")

    def get_one(
        self, query: str, params: Tuple | dict = ()
    ) -> Optional[Dict[Any, Any]]:
        """
        Funcao de retirar apenas uma entrada da tabela.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            row = cursor.fetchone()
            return dict(row) if row else None

    def get_many(self, query: str, params: Tuple | dict[str, Any] = ()) -> List[Dict]:
        """
        Funcao de retirar varias entradas da tabela (Inclusive get_all).
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def update(self, query: str, params: Tuple | dict = ()) -> int:
        """
        Funcao que modifica parametros de linhas da tabela.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount

    def delete(self, query: str, params: Tuple | dict = ()) -> int:
        """
        Funcao que deleta uma linha da tabela.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount
