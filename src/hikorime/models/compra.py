from datetime import date
from hikorime.models.tipopagamento import TipoPagamento

class Compra:
    def __init__(self, data_compra, valor_total, pagamento: TipoPagamento):
        self.data_compra = data_compra
        self.valor_total = valor_total
        pagamento = pagamento
   
   #Encapsulamento dos atributos
    @property
    def data_compra(self):
        return self.__data_compra
    
    @data_compra.setter
    def data_compra(self, data_compra_valida):
        if not isinstance(data_compra_valida, date):
            raise ValueError("Tipo inválido! O valor deve ser uma data!")
        else:
            self.__data_compra = data_compra_valida

    @property
    def valor_total(self):
        return self.__valor_total
    
    @valor_total.setter
    def valor_total(self, valor_total_valido):
        if not isinstance(valor_total_valido, float):
            raise ValueError("O valor total deve ser numérico")
        else:
            self.__valor_total = valor_total_valido