from pydantic import BaseModel

class Aeronave(BaseModel):
    modelo: str
    total_assentos: int
