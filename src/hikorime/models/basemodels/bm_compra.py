from pydantic import BaseModel

from hikorime.models.enums.tipo_pagamento import TipoPagamento

class Compra(BaseModel):
    #base de compra - lado do usuario
    id_passagem: int
    id_cupom: int
    id_bagagem: int
    valor_pago: float
    tipo_pagamento: TipoPagamento