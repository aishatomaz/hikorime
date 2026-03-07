from enum import Enum

'''A especificação do tipo de bagagem tem como objetivo a garantia a segurança dos bens materiais e dos direitos dos passageiros,
evitando o manuseio inadequado.'''

class TipoBagagem(Enum):
    FRAGIL = "frágil"
    NORMAL = "normal"

    @classmethod
    def enum_to_dict(cls):
        """
        Converte o Enum para um dicionário
        """
        return {item.name: item.value for item in cls}