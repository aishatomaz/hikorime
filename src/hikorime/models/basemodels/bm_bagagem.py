from pydantic import BaseModel, Field
from models.enums.tipo_bagagem import TipoBagagem
class Bagagem(BaseModel):
     #modelo de entrada da classe de bagagem para fastapi utilizando a biblioteca pydantic
     peso: float
     tipo: TipoBagagem = Field(...) #aceita o formato do enum 
   