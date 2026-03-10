from pydantic import BaseModel

class Aeronave(BaseModel):
    """
        Modelo de aeronave 

        Args: 
            modelo (str): modelo da aeronave
            total_assentos (int): total de assentos da aeronave
        Returns:
            Aeronave: modelo de aeronave
    """
    modelo: str
    total_assentos: int
