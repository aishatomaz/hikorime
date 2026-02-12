from .compra import Compra
from .enums.tipo_pagamento import TipoPagamento
from .passagem import Passagem
from .voo import voo


class Notificacao:
    def __init__(
        self,
        passagem: Passagem,
        compra: Compra,
        voo: voo,
        pagamento: TipoPagamento,
        prox_partida=False,
    ):

        self.passagem = passagem
        self.compra = compra
        self.voo = voo
        self.prox_partida = prox_partida
        self.pagamento = pagamento
