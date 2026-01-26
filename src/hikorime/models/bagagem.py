from tipobagagem import TipoBagagem
from pagamento import Pagamento
class Bagagem:
    def __init__(self, peso, tipo: TipoBagagem, confirmacao = False):
        self.peso = peso
        self.tipo = tipo
        self.confirmacao = confirmacao


    #getters e setters
    @property 
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso_valido):
        if not isinstance(peso_valido,int, float):
            raise ValueError ("O peso deve ser representado por um valor numérico")
        elif self.__peso > 10:
            raise ValueError("Sua bagagem ultrapassa o limite de carga por passageiro, limite: 10 KG")
        else:
            self.__peso = peso_valido

    @property
    def confirmacao(self):
        pass
    def registrar_bagagem():
        #para registrar a bagagem será necessário uma confirmação 

        if self.confirmacao == True:
            #salvar no banco de dados 

            pass

