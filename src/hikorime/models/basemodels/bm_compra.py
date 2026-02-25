
from pydantic import BaseModel

class CompraPassagem(BaseModel):
    #base de compra passagem - lado do usuario
    assento: int
    id_voo: int
    id_passageiro: int
    valor_pago: float
