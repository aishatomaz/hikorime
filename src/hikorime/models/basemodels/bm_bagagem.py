from pydantic import BaseModel, Field
from hikorime.models.enums.tipo_bagagem import TipoBagagem

class Bagagem(BaseModel):
    """
    Modelo de bagagem para o sistema de gerenciamento de bagagens do aeroporto.

    Args: 
        peso (float): O peso da bagagem em kg.
        valor_bagagem (float): O valor da bagagem em reais.
        tipo (TipoBagagem): O tipo da bagagem, que pode ser de mão, despachada ou especial. 

    Returns:
        Bagagem: Um objeto do tipo Bagagem com os atributos definidos.
    """
    # modelo de entrada da classe de bagagem para fastapi utilizando a biblioteca pydantic
    peso: float
    valor_bagagem: float
    tipo: TipoBagagem = Field(...) #aceita o formato do enum
