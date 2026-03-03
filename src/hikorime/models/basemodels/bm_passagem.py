
from pydantic import BaseModel

class CompraPassagem(BaseModel):
    #base de compra passagem - lado do usuario
    id_voo: int
    id_passageiro: int
    assento: int
