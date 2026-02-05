from tipo_pagamento import TipoPagamento

class Pagamento:
    def __init__(self, valor, pagamento: TipoPagamento):
        self.valor = valor
        self.pagamento = pagamento

    #Encapsulamento dos atributos
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor_valido):
        if not isinstance(valor_valido, float):
            raise ValueError("Tipo inválido! O valor deve ser numérico.")
        else:
            self.__valor = valor_valido