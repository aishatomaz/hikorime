from pydantic import BaseModel, Field
from datetime import date
from hikorime.models.enums.status_cupom import StatusCupom


class Cupom(BaseModel):
    # base para cadastro de cupons no sistema
    id_cupom: int
    percentual_desconto: float
    validade: date
    status: StatusCupom = Field(...)

