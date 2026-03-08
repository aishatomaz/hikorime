from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Passagem(BaseModel):
    """
    Base de compra passagem - lado do usuário.

    Args:
        id_voo (int): ID do voo para o qual a passagem foi comprada.
        id_passageiro (int): ID do passageiro que comprou a passagem.
        assento (str): Assento reservado para o passageiro.
        valor_pago (Optional[float]): Valor pago pela passagem. Padrão é 0.0.
        data_compra (Optional[datetime]): Data e hora da compra da passagem. Padrão é None.
    Returns:
        Passagem: Instância da classe Passagem com os dados fornecidos.
    """
    
    id_voo: int
    id_passageiro: int
    assento: str
    valor_pago: Optional[float] = 0.0
    data_compra: Optional[datetime] = None