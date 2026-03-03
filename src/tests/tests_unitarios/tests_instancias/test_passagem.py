import pytest
from hikorime.models.passagem import Passagem

#tem um problema na classe passagem - importação circular pois passagem chama notificacao e notificação 
# chama passagem simultaneamente o que causa comflito nos testes - por favor corrigir isso.

def test_passagem():
    '''
    testa instancia de passagem
    '''
    passagem = Passagem(
        assento= 1, valor_final = 100
    )
    assert passagem