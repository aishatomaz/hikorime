from pydantic import BaseModel
from datetime import datetime

class Voo(BaseModel):
    #dados do voo - rota de comissario recebera para cadastrar voo
    data_hora_partida: datetime
    data_hora_chegada: datetime
    local_origem: str
    local_destino: str
    assentos_ocupados: int
    valor_passagens: float # TODO: remover
    # TODO: assentos totais
    # TODO: id_aviao