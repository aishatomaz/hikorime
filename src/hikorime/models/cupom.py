'''...'''

from datetime import date, datetime

class Cupom:
    def __init__(self, percentual_desconto, validade):
        self.percentual_desconto = percentual_desconto
        self.validade = validade

    @property
    def percentual_desconto(self):
        return self._percentual_desconto
    
    @percentual_desconto.setter
    def percentual_desconto(self, percentual_desconto_valido):
        if not isinstance (percentual_desconto_valido, (int, float)):
            raise TypeError("Tipo inválido! O tipo deve ser numérico!")
        else:
            self._percentual_desconto = percentual_desconto_valido    


    def verificar_disponibilidade_cupom(self):
        return
    
    def verificar_validade_cupom(self):
        return
    
    def aplicar_cupom(self):
        return

#Instância   
cupom = Cupom("asdfghjk", "22/07/2030")
print(cupom.percentual_desconto)
print(cupom.validade)