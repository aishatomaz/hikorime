import pytest
from hikorime.models.passagem import Passagem

def test_passagem():
    '''
    testa instancia de passagem
    '''
    passagem = Passagem(
        assento= 1, valor_final = 100, notificacao=None
    )
    assert passagem
