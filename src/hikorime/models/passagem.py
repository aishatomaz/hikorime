from hikorime.models.notificacao import Notificacao


'''
A passagem comprada pelo passageiro deve informar o assento e o valor da passagem. Após a compra, o passageiro receberá uma notificação.
'''
class Passagem:
    def __init__(self, assento, valor_final, notificacao: Notificacao):
        self.assento = assento
        self.valor_final = valor_final
        self.notificacao = notificacao

    # Encapsulamento dos atributos
    @property
    def assento(self):
        return self.__assento

    @assento.setter
    def assento(self, assento_valido):
        if not isinstance(assento_valido, int):
            raise ValueError("Número de assento inválido")
        else:
            self.__assento = assento_valido

    @property
    def valor_final(self):
        return self.__valor_final

    @valor_final.setter
    def valor_final(self, valor_final_valido):
        if not isinstance(valor_final_valido, float):
            raise ValueError("Valor final inválido! O valor deve ser numérico!")
        else:
            self.__valor_final = valor_final_valido

    def verificar_disponibilidade_assento(self):
        return

    def escolher_assento(self):
        return
