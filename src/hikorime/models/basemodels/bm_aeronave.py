from pydantic import BaseModel

class Aeronave(BaseModel):
    id_aeronave: int
    modelo: str
    total_assentos: int
    terminal: str
    portal_embarque: str