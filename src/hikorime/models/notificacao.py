from .compra import Compra
from .enums.tipo_pagamento import TipoPagamento
from .voo import Voo

class Notificacao:
    def __init__(
        self,
       # passagem: Passagem, //tava gerando erro de importação circular impedindo testes, verifiquem se realmente é necessária
       #essa importação de passagem
        compra: Compra,
        voo: Voo,
        pagamento: TipoPagamento,
        prox_partida=False,
    ):

        #self.passagem = passagem
        self.compra = compra
        self.voo = voo
        self.prox_partida = prox_partida
        self.pagamento = pagamento
