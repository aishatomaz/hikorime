from enum import Enum

'''A especificação do tipo de bagagem tem como objetivo a garantia a segurança dos bens materiais e dos direitos dos passageiros,
evitando o manuseio inadequado.'''

class TipoBagagem(Enum):
    FRAGIL = "FRAGIL"
    NORMAL = "NORMAL"