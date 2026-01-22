'''...'''

from tipo_pagamento import TipoPagamento

class Pagamento:
    def __init__(self, valor, pagamento: TipoPagamento):
        self.valor = valor
        self.pagamento = pagamento

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor_valido):
        if not isinstance(valor_valido, (float, int)):
            raise TypeError("Tipo inválido!")
        else:
            self._valor = valor_valido