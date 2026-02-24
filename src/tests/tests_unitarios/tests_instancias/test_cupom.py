import pytest
from hikorime.models.cupom import Cupom
from datetime import date

def test_cupom():
    """Instância de teste do model cupom"""
    cupom = Cupom(percentual_desconto=0.25, validade=date(2026, 6, 6), status="DISPONIVEL")
    assert cupom