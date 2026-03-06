from enum import Enum

class TipoPassaporte(Enum):
    COMUM = "comum"
    EMERGENCIA = "emergência"
    DIPLOMATICO = "diplomático"
    ESTRANGEIRO = "estrangeiro"

    @classmethod
    def enum_to_dict(cls):
        """
        Converte o Enum para um dicionário
        """
        return {item.name: item.value for item in cls}

