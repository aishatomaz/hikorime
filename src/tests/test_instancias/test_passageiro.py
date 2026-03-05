import pytest
from hikorime.models.basemodels.bm_passageiro import Passageiro
from hikorime.models.enums.tipo_usuario import TipoUsuario

def test_criar_passageiro():
    """
    Testa a criação de uma instância de Passageiro com dados válidos.
    """
    passageiro = Passageiro(
        nome="Maria Souza",
        email="maria.souza@example.com",
        cpf="10987654321",
        senha="senha456",
        passaporte="BR123456"
    )
    assert passageiro.nome == "Maria Souza"
    assert passageiro.email == "maria.souza@example.com"
    assert passageiro.cpf == "10987654321"
    assert passageiro.senha == "senha456"
    assert passageiro.tipo == TipoUsuario.PASSAGEIRO
    assert passageiro.passaporte == "BR123456"
