
from pydantic import BaseModel

class Passagem(BaseModel):
    #base de compra passagem - lado do usuario
    id_voo: int
    id_passageiro: int
    assento: int
