from enum import Enum

'''O aeroporto aceita três tipos de pagamento na compra, como estabelecido nas regras de negócio.'''
class TipoPagamento(Enum):
    PIX = "PIX"
    DEBITO = "DEBITO"
    CREDITO = "CREDITO"
