import pytest
from datetime import date
from hikorime.models.cupom import Cupom
from hikorime.models.enums.status_cupom import StatusCupom

def test_percentual_desconto_int():
    """Verifica se o percentual de desconto é um valor inteiro"""
    with pytest.raises(ValueError, match="Tipo inválido"):
        Cupom(10, date.today(), StatusCupom)

def test_percentual_desconto_string():
    """Verifica se o percentual de desconto é uma string"""
    with pytest.raises(ValueError):
        Cupom("10.5", date.today(), StatusCupom)

def test_percentual_desconto_none():
    """Verifica se o percentual de desconto é um valor nulo"""
    with pytest.raises(ValueError):
        Cupom(None, date.today(), StatusCupom)

def test_validade_string():
    """Verifica se a validade inserida foi uma string"""
    with pytest.raises(ValueError):
        Cupom(10.0, "2026-12-31", StatusCupom)

def test_validade_int():
    """Verifica se a validade inserida foi um inteiro"""
    with pytest.raises(ValueError):
        Cupom(10.0, 20261231, StatusCupom)

def test_validade_none():
    """Verifica se a validade inserida é nula"""
    with pytest.raises(ValueError):
        Cupom(10.0, None, StatusCupom)
