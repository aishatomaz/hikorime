from pydantic import BaseModel, Field
from datetime import date
from models.enums.status_cupom import StatusCupom
class Cupom(BaseModel):
    #base para cadastro de cupons no sistema
    percentual_desconto: float
    validade: date
    status: StatusCupom = Field(...)