'''...'''

from datetime import date

class Compra:
    def __init__(self, data_compra, valor_total):
        self.data_compra = data_compra
        self.valor_total = valor_total

    @property
    def valor_total(self):
        return self._valor_total
    
    @valor_total.setter
    def valor_total(self, valor_total_valido):
        if not isinstance(valor_total_valido, (int, float)):
            raise TypeError("O valor total deve ser numérico")
        else:
            self._valor_total = float(valor_total_valido)