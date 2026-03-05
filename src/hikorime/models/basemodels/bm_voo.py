from pydantic import BaseModel
from datetime import datetime

class Voo(BaseModel):
    #dados do voo - rota de comissario recebera para cadastrar voo
    id_aeronave: int
    data_hora_partida: datetime
    data_hora_chegada: datetime
    local_origem: str
    local_destino: str
    terminal: str
    portao_embarque: str
    valor_base_passagem: float
    