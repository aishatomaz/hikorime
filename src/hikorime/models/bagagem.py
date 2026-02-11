from hikorime.models.enums.tipo_bagagem import TipoBagagem
from hikorime.models.enums.const_bagagens import ConstantesBagagem

dados = ConstantesBagagem


class Bagagem:
    def __init__(self, peso, tipo: TipoBagagem, confirmacao=False):

        # TODO: Valor_fixo e valor_bagagem, esta hard coded aqui, coloque em um enum, ou em um config.py (Dhonatan)

        self.peso = peso
        self.tipo = tipo
        self.confirmacao = confirmacao
        self.valor_fixo = 50.00
        self.valor_bagagem = 0

    # getters e setters
    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso_valido):
        try:
            float(peso_valido)
        except ValueError:  # Removido 'as erro', ja que nao estava a ser usado
            raise ValueError("O peso deve ser representado por um valor numérico")
        if peso_valido > dados.PESO_MAXIMO:
            raise ValueError(
                f"Sua bagagem ultrapassa o limite de carga por passageiro, limite: {dados.PESO_MAXIMO} KG"
            )
        else:
            self.__peso = peso_valido

    def calcular_valor_bagagem(self):
        taxa_variavel = self.__peso * 5
        self.valor_bagagem = self.valor_fixo + taxa_variavel

    def registrar_bagagem(self):
        # para registrar a bagagem será necessário uma confirmação

        if self.confirmacao is True:
            # salvar no banco de dados peso, tipo, valor e id do passageiro

            pass
