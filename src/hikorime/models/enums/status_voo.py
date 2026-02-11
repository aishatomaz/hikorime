from enum import Enum


'''Os Status são fundamentais para facilitar as compras das passagens e a visualização dos voos.'''
class StatusVoo(Enum):
    DISPONIVEL = "DISPONIVEL"
    ESGOTADO = "ESGOTADO"
    INDISPONIVEL = "INDISPONIVEL"