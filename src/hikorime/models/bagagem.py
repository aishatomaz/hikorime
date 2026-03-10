from hikorime.models.enums.tipo_bagagem import TipoBagagem
from hikorime.models.enums.const_bagagens import ConstantesBagagem

class Bagagem:
    """
    Bagagem especifíca o tipo e o peso da bagagem que o passageiro irá levar. A bagagem possuí um valor defindido e o valor não pode ser superior à 10kg,
    os valores são estabelecidos pelas regras de negócio.
    """
    def __init__(self, peso, tipo: TipoBagagem, confirmacao=False):

        self.peso = peso
        self.tipo = tipo
        self.confirmacao = confirmacao
        self.valor_fixo = ConstantesBagagem.VALOR_FIXO
        self.valor_bagagem = 0

    # getters e setters
    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso_valido):
        try:
            float(peso_valido)
        except ValueError:  
            raise ValueError("O peso deve ser representado por um valor numérico")
        if peso_valido > ConstantesBagagem.PESO_MAXIMO.value:
            raise ValueError(
                f"Sua bagagem ultrapassa o limite de carga por passageiro, limite: {ConstantesBagagem.PESO_MAXIMO} KG"
            )
        else:
            self.__peso = peso_valido

    def calcular_valor_bagagem(self):
        taxa_variavel = self.__peso * ConstantesBagagem.TAXA_VARIAVEL
        self.valor_bagagem = self.valor_fixo + taxa_variavel

 