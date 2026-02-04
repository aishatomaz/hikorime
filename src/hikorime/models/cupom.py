from datetime import date

class Cupom:
    def __init__(self, percentual_desconto, validade):
        self.percentual_desconto = percentual_desconto
        self.validade = validade

    #Encapsulamento dos atributos
    @property
    def percentual_desconto(self):
        return self.__percentual_desconto
    
    @percentual_desconto.setter
    def percentual_desconto(self, percentual_desconto_valido):
        if not isinstance (percentual_desconto_valido, float):
            raise ValueError("Tipo inválido! O tipo deve ser numérico!")
        else:
            self.__percentual_desconto = percentual_desconto_valido  

    @property
    def validade(self):
        return self.__validade
    
    @validade.setter
    def validade(self, validade_valida):
        if not isinstance (validade_valida, date):
            raise ValueError("Tipo inválido! O tipo deve ser numérico!")
        else:
            self.__validade = validade_valida

    def verificar_possibilidade_cupom(self):
        return
        
    def verificar_validade_cupom(self):
        return
    
    def aplicar_cupom(self):
        return