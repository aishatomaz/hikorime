import pytest
from hikorime.models.basemodels.bm_funcionario import Funcionario
from hikorime.models.enums.tipo_usuario import TipoUsuario
from datetime import date

def test_criar_funcionario():
    """
    Testa a criação de uma instância de Funcionario com dados válidos.
    """
    funcionario = Funcionario(
        nome="João Silva",
        email="joao.silva@example.com",
        data_nascimento=date(2000, 3, 10),
        cpf="12345678901",
        senha="senha123",
        tipo_usuario=TipoUsuario.FUNCIONARIO,
        cargo="Gerente",
        matricula="FNC001"
    )
    assert funcionario.nome == "João Silva"
    assert funcionario.email == "joao.silva@example.com"
    assert funcionario.cpf == "12345678901"
    assert funcionario.senha == "senha123"
    assert funcionario.tipo_usuario == TipoUsuario.FUNCIONARIO
    assert funcionario.cargo == "Gerente"
    assert funcionario.matricula == "FNC001"
