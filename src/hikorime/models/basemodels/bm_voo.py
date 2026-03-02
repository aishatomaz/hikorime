from pydantic import BaseModel
from datetime import datetime

class Voo(BaseModel):
    #dados do voo - rota de comissario recebera para cadastrar voo
    id_voo: int
    data_partida: datetime
    data_hora_chegada: datetime
    local_origem: str
    local_destino: str
    id_aeronave: int
    