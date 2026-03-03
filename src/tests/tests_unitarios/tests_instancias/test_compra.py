import pytest
from hikorime.models.compra import Compra
from datetime import date

def test_compra():
    '''
    testa instancia de compra
    '''
    compra = Compra(
        data_compra = date(2026, 1, 2), valor_total = 100, pagamento = "PIX"
    )
    assert compra