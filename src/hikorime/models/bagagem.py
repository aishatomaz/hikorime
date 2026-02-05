from hikorime.models.enums.tipobagagem import TipoBagagem
from hikorime.service.const_bagagens import ConstantesBagagem

dados = ConstantesBagagem()

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
        try:
            float(peso_valido)
        except ValueError as erro:
            raise ValueError ("O peso deve ser representado por um valor numérico")
        if peso_valido > dados.peso_maximo:
            raise ValueError(f"Sua bagagem ultrapassa o limite de carga por passageiro, limite: {dados.peso_maximo} KG")
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

