from pydantic import BaseModel


class CompraPassagem(BaseModel):
    assento: int
    id_voo: int
    id_passageiro: int
    valor_pago: float
