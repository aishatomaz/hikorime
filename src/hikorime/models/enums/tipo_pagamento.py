from enum import Enum

'''O aeroporto aceita três tipos de pagamento na compra, como estabelecido nas regras de negócio.'''
class TipoPagamento(Enum):
    PIX = "pix"
    DEBITO = "débito"
    CREDITO = "crédito"

    @classmethod
    def enum_to_dict(cls) -> dict[str, str]:
        """
        Converte o Enum para um dicionário
        """
        return {item.name: item.value for item in cls}