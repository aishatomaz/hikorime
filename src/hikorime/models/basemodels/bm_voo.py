from pydantic import BaseModel
from datetime import datetime

class Voo(BaseModel):
    """
    Modelo de dados para representar um voo.

    Args: 
        id_aeronave (int): Identificador da aeronave associada ao voo.
        data_hora_partida (datetime): Data e hora de partida do voo.
        data_hora_chegada (datetime): Data e hora de chegada do voo.
        local_origem (str): Local de origem do voo.
        local_destino (str): Local de destino do voo.
        terminal (str): Terminal de embarque do voo.
        portao_embarque (str): Portão de embarque do voo.
        valor_base_passagem (float): Valor base da passagem para o voo.
    
    Returns:
        Voo: Instância do modelo de dados do voo.
    """

    # dados do voo - rota de comissario recebera para cadastrar voo
    id_aeronave: int
    data_hora_partida: datetime
    data_hora_chegada: datetime
    local_origem: str
    local_destino: str
    terminal: str
    portao_embarque: str
    valor_base_passagem: float
    
    
