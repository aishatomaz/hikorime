from hikorime.models.voo import Voo
from datetime import datetime 
import pytest

def test_voo():
    """
    Instancia de voo
    """
    voo = Voo(
        data_hora_partida=datetime(2026, 1, 2, 10, 12), data_hora_chegada=datetime(2026, 1, 5, 14, 30), 
        local_origem="Bahia", local_destino="Mauriti", assentos_ocupados=50, valor_passagens=150
    )
    assert voo