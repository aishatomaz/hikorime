import pytest
from datetime import date

from hikorime.models.basemodels.bm_passageiro import Passageiro
from hikorime.models.enums.tipo_usuario import TipoUsuario
from hikorime.models.enums.tipo_passaporte import TipoPassaporte

def test_criar_passageiro():
    """
    Testa a criação de uma instância de Passageiro com dados válidos.
    """
    passageiro = Passageiro(
        nome="Maria Souza",
        email="maria.souza@example.com",
        data_nascimento=date(2020, 1, 1),
        cpf="10987654321",
        senha="senha456",
        codigo_passaporte="BR123456",
        tipo_passaporte=TipoPassaporte.COMUM,
    )
    assert passageiro.nome == "Maria Souza"
    assert passageiro.email == "maria.souza@example.com"
    assert passageiro.data_nascimento == date(2020, 1, 1)
    assert passageiro.cpf == "10987654321"
    assert passageiro.senha == "senha456"
    assert passageiro.tipo_usuario == TipoUsuario.PASSAGEIRO
    assert passageiro.codigo_passaporte == "BR123456"
    assert passageiro.tipo_passaporte == TipoPassaporte.COMUM
