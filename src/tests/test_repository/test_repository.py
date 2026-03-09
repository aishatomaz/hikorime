from pathlib import Path
import pytest
from unittest.mock import patch
from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.repository.repository_connection import RepositoryConnection
import sqlite3


@pytest.fixture()
def mock_db_setup(tmp_path):
    # 1. Configuração de caminhos temporários
    db_file = tmp_path / "test_db.db"
    schema_file = tmp_path / "schema.sql"

    # 2. Definição e criação do Schema
    schema_content = """
    DROP TABLE IF EXISTS test_users;
    CREATE TABLE test_users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT
    );
    """
    schema_file.write_text(schema_content, encoding="utf-8")

    # 3. Inicialização física do banco (Aplica o schema no arquivo temporário)
    # Isso garante que a tabela exista antes do repositório tentar acessá-la
    with sqlite3.connect(db_file) as conn:
        conn.executescript(schema_content)

    path_conn = "hikorime.repository.repository_connection"
    path_repo = "hikorime.repository.repository_querys"

    # 4. Patch das constantes e da classe de conexão
    # Patchamos o DATABASE_PATH no módulo de conexão para que o RepositoryConnection()
    # aponte para o arquivo temporário que acabamos de criar.
    with (
        patch(f"{path_conn}.DATABASE_PATH", str(db_file)),
        patch(f"{path_conn}.SCHEMA_PATH", str(schema_file)),
    ):
        # Instanciamos o repo que usará a conexão apontando para o banco temporário
        repo = RepositoryQuerys("test_users")
        yield repo

    # O Pytest removerá o diretório tmp_path automaticamente depois


class TestRepositoryQuerys:
    def test_save_success(self, mock_db_setup):
        repo = mock_db_setup
        # Testa o insert
        last_id = repo.save(name="Invers", email="invers@teste.com")

        assert last_id == 1

        # Verifica se foi salvo mesmo
        user = repo.get_by_id(1)
        assert user["name"] == "Invers"

    def test_save_invalid_column_raises_error(self, mock_db_setup):
        repo = mock_db_setup
        with pytest.raises(ValueError, match="Nome de coluna inválido"):
            repo.save(**{"coluna; DROP TABLE users; --": "valor"})

    def test_get_all(self, mock_db_setup):
        repo = mock_db_setup
        repo.save(name="User 1")
        repo.save(name="User 2")

        results = repo.get_all()
        assert len(results) == 2

    def test_get_by_column_name(self, mock_db_setup):
        repo = mock_db_setup
        repo.save(name="Python", email="py@test.com")

        result = repo.get_by_column_name("name", "Python")
        assert result is not None
        assert result["email"] == "py@test.com"

    def test_get_like_by_column_name(self, mock_db_setup):
        repo = mock_db_setup
        repo.save(name="Hikorime Project")

        # Busca parcial
        result = repo.get_like_by_column_name("name", "kori")
        assert result is not None
        assert "Hikorime" in result["name"]

    def test_delete_by_id(self, mock_db_setup):
        repo = mock_db_setup
        repo.save(name="To be deleted")

        rows_affected = repo.delete_by_id(1)
        assert rows_affected == 1

        result = repo.get_by_id(1)
        assert result is None

    def test_put_in_table(self, mock_db_setup):
        repo = mock_db_setup
        repo.save(name="Old Name", email="old@test.com")

        # Atualiza apenas o nome
        repo.put_in_table(1, {"name": "New Name"})

        updated_user = repo.get_by_id(1)
        assert updated_user["name"] == "New Name"
        assert updated_user["email"] == "old@test.com"

    def test_get_quantity_of_rown(self, mock_db_setup):
        repo = mock_db_setup
        repo.save(name="A")
        repo.save(name="B")
        repo.save(name="C")

        res = repo.get_quantity_of_rown()
        count = list(res.values())[0]
        assert count == 3
