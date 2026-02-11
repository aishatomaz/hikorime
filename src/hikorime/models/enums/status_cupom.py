from enum import Enum

'''Mostra todos os estados possíveis em relação à disponibilidade dos cupons. Útil para garantir as regras de negócio.'''

class StatusCupom(Enum):
    DISPONIVEL = "DISPONIVEL"
    INDISPONIVEL = "INDISPONIVEL"
    EXPIRADO = "EXPIRADO"