import pytest
from datetime import date
from pydantic import BaseModel, EmailStr, Field
from hikorime.models.basemodels.bm_funcionario import Funcionario
from hikorime.models.enums.tipo_usuario import TipoUsuario

def test_criar_funcionario():
    """
    Testa a criação de uma instância de Funcionário com dados válidos.
    """
    funcionario = Funcionario(
        nome="João Silva",
        data_nascimento=date(2020, 1, 1),
        email="joao.silva@example.com",
        cpf="12345678901",
        senha="senha123",
        cargo="Gerente",
        matricula="FNC001"
    )
    assert funcionario.nome == "João Silva"
    assert funcionario.data_nascimento == date(2020, 1, 1)
    assert funcionario.email == "joao.silva@example.com"
    assert funcionario.cpf == "12345678901"
    assert funcionario.senha == "senha123"
    assert funcionario.tipo_usuario == TipoUsuario.FUNCIONARIO
    assert funcionario.cargo == "Gerente"
    assert funcionario.matricula == "FNC001"