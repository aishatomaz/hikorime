from pydantic import BaseModel
from datetime import datetime


class VooBase(BaseModel):
    data_hora_partida: datetime
    data_hora_chegada: datetime
    local_origem: str
    local_destino: str
    assentos_ocupados: int # TODO!: a cada nova passagem, atualizar no DB