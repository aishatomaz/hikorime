import pytest
from hikorime.models.basemodels.bm_login import login_request

def test_criar_login_request():
    """
    Testa a criação de uma instância de login_request com dados válidos.
    """
    login = login_request()
    login.email = "teste@example.com"
    login.senha = "minhasenha"

    assert login.email == "teste@example.com"
    assert login.senha == "minhasenha"