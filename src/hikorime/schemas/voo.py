from datetime import date, time
from pydantic import BaseModel


class VooModelo(BaseModel):
    data_saida: date
    data_cheg: date
    hora_saida: time
    hora_chega: time
    local_saida: str
    destino: str
    id_piloto: int
    aviao: str  # Mudei de int para str (Dhonatan)
    quant_vagas: int
