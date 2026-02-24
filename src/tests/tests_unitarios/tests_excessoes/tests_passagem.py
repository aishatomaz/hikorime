import pytest
from unittest.mock import Mock
from hikorime.models.passagem import Passagem
from hikorime.models.notificacao import Notificacao

def test_assento_string():

    """Verifica se o assento foi informado com valor de string"""
    notificacao_mock = Mock(spec=Notificacao)

    with pytest.raises(ValueError, match="Número de assento inválido"):
        Passagem("A12", 500, notificacao_mock)

def test_assento_float():
    """Verifica se o assento foi informado com valor de ponto flutuante"""
    notificacao_mock = Mock(spec=Notificacao)

    with pytest.raises(ValueError):
        Passagem(12.5, 500, notificacao_mock)

def test_assento_none():
    """Verifica se o assento informado foi nulo"""
    notificacao_mock = Mock(spec=Notificacao)

    with pytest.raises(ValueError):
        Passagem(None, 500, notificacao_mock)

def test_valor_final_invalido():
    """Verifica se uma excessao é lançada quando o valor é invalido """
    notificacao_mock = Mock(spec=Notificacao)

    with pytest.raises(ValueError):
        Passagem(10, object(), notificacao_mock)