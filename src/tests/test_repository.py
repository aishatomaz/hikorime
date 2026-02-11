from hikorime.repository.repository_connection import RepositoryConnection

'''O Objetivo desses testes é verificar se as operações básicas estão funcionando corretamente.'''

def test_repository(tmp_path):
    # Caminho temporário para o pytest
    db_path = tmp_path / "test.db"

    repo = RepositoryConnection(db_path)

    # Criando tabela
    repo.query("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT
        );
    """)

    # Inserindo dado
    repo.query(
        """
        INSERT INTO users (id, name) VALUES (:id, :name);
    """,
        {"id": 1, "name": "sudo_invers"},
    )  # Aproveitando, e testando a insercao dicionario

    # Buscando dado
    result = repo.query("""
        SELECT * FROM users;
    """)

    # Validações
    assert db_path.exists()
    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["name"] == "sudo_invers"
