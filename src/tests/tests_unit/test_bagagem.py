import pytest
from hikorime.models.bagagem import Bagagem

def test_calculo_bagagem():
    bagagem = Bagagem(
        peso=2,  tipo="FRAGIL", confirmacao=True
    )
    bagagem.calcular_valor_bagagem()
    assert bagagem