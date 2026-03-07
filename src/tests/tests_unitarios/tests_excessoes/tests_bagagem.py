import pytest
from hikorime.models.bagagem import Bagagem
from hikorime.models.enums.tipo_bagagem import TipoBagagem
from hikorime.models.enums.const_bagagens import ConstantesBagagem

def test_peso_nao_numerico():
    """verifica se o peso é de tipo errado"""
    with pytest.raises(ValueError):
        Bagagem("abc", TipoBagagem.NORMAL)


def test_peso_acima_limite():
    """verifica se o peso é maior do que o permitido"""
    limite = ConstantesBagagem.PESO_MAXIMO.value
    with pytest.raises(ValueError):
        Bagagem(limite + 1, TipoBagagem.NORMAL)


def test_peso_no_limite():
    """verifica se o peso digitado é o peso maximo"""
    limite = ConstantesBagagem.PESO_MAXIMO.value
    bagagem = Bagagem(limite, TipoBagagem.NORMAL)
    assert bagagem.peso == limite
