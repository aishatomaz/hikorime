import pytest
from hikorime.models.basemodels.bm_login import LoginRequest

def test_criar_login_request():
    """
    Testa a criação de uma instância de login_request com dados válidos.
    """
    login = LoginRequest(
        email = "teste@example.com",
        senha = "minhasenha"
    )

    assert login.email == "teste@example.com"
    assert login.senha == "minhasenha"