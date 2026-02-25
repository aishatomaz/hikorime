from pydantic import BaseModel, Field

class Passagem(BaseModel):
    #modelo de entrada de dados de passagem - lado do comissario
    assento: int
    valor_final: float