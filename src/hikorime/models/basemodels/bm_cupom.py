from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
from hikorime.models.enums.status_cupom import StatusCupom


class Cupom(BaseModel):
    """
    Base para cadastro de cupons no sistema.

    Args: 
        id_passageiro (int): ID do passageiro associado ao cupom.
        percentual_desconto (float): Percentual de desconto oferecido pelo cupom.
        validade (date): Data de validade do cupom.
        status (StatusCupom, opcional): Status atual do cupom. Padrão é DISPONIVEL.
        usado (int, opcional): Indica se o cupom já foi usado. Padrão é 0 (não usado).
        id_cupom (int, opcional): ID do cupom, caso seja necessário para identificação futura.
   
    Returns:
        Cupom: Instância do cupom criado.
    """
    
    id_passageiro: int
    percentual_desconto: float
    validade: date
    status: StatusCupom = Field(default=StatusCupom.DISPONIVEL)
    usado: int = Field(default=0)
    id_cupom: Optional[int] = None
