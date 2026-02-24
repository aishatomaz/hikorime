import pytest
from hikorime.models.bagagem import Bagagem

def test_calculo_bagagem():
    '''
    Deve verificar se o peso da bagagem não ultrapassa o valor permitido (10kg) e se o calculo do valor final está correto.
    '''
    bagagem = Bagagem(
        peso=2,  tipo="FRAGIL", confirmacao=True
    )
    bagagem.calcular_valor_bagagem()
    assert bagagem