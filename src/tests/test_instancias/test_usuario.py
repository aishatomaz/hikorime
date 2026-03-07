import pytest
from hikorime.models.basemodels.bm_usuario import UsuarioBase
from hikorime.models.enums.tipo_usuario import TipoUsuario

def test_criar_usuario_base():
    """
    Testa a criação de uma instância de UsuarioBase com dados válidos.
    """
    usuario = UsuarioBase(
        nome="Carlos Santos",
        email="carlos.santos@example.com",
        cpf="11223344556",
        senha="senha789",
        tipo_usuario=TipoUsuario.PASSAGEIRO
    )
    assert usuario.nome == "Carlos Santos"
    assert usuario.email == "carlos.santos@example.com"
    assert usuario.cpf == "11223344556"
    assert usuario.senha == "senha789"
    assert usuario.tipo_usuario == TipoUsuario.PASSAGEIRO
