from datetime import date
from hikorime.models.enums.tipo_pagamento import TipoPagamento

'''
Classe Compra recebe o valor total de todas as compras (no caso, o valor da passagem, junto do valor da babagem e o desconto do cupom, se possível),
seleciona o tipo de pagamento, sendo a compra final.
'''
class Compra:
    def __init__(self, data_compra, valor_total, pagamento: TipoPagamento):
        self.data_compra = data_compra
        self.valor_total = valor_total
        pagamento = pagamento

    @property
    def data_compra(self):
        return self.__data_compra

    @data_compra.setter
    def data_compra(self, data_compra_valida):
        if not isinstance(data_compra_valida, date):
            raise ValueError("O valor deve ser uma data data válida!")
        else:
            self.__data_compra = data_compra_valida

    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor_total_valido):
        try:
            float(valor_total_valido)
        except ValueError:  # Removido 'as erro', ja que nao estava a ser usado
            raise ValueError("O valor total deve ser representado por um valor numérico")
        else:
            self.__valor_total = valor_total_valido

