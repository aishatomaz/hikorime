from pathlib import Path
import pytest
from unittest.mock import patch
from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.repository.repository_connection import RepositoryConnection


@pytest.fixture()
def mock_db_setup(tmp_path):
    """
    Configura um banco SQLite temporário, aplica o schema
    e isola as constantes globais durante o teste.
    """
    db_file = Path(tmp_path / "test_db.db")
    schema_file = Path(tmp_path / "schema.sql")

    schema_content = """
    DROP TABLE IF EXISTS test_users;
    CREATE TABLE IF NOT EXISTS test_users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT
    );
    """
    schema_file.write_text(schema_content, encoding="utf-8")

    path_repo = "hikorime.repository.repository_querys"
    path_conn = "hikorime.repository.repository_connection"

    with (
        # Alterei as constantes no arquivo de conexao original para o teste
        patch(f"{path_conn}.DATABASE_PATH", str(db_file)),
        patch(f"{path_conn}.SCHEMA_PATH", str(schema_file)),
        # Garante que use a classe com os novos paths.
        patch(f"{path_repo}.RepositoryConnection") as MockConn,
    ):
        # Configura o mock para se comportar como uma conexao real,
        # mas usando os paths que injetamos acima.
        MockConn.return_value = RepositoryConnection()

        repo = RepositoryQuerys("test_users")

        yield repo


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
