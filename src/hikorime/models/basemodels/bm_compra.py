from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from hikorime.models.enums.tipo_pagamento import TipoPagamento


class Compra(BaseModel):
    """
    Representa uma compra de passagem realizada por um usuário.

    Args:
        id_passageiro (int): ID do passageiro que realizou a compra.
        id_passagem (int): ID da passagem comprada.
        id_bagagem (Optional[int]): ID da bagagem associada à compra, se houver.
        id_cupom (Optional[int]): ID do cupom de desconto aplicado à compra, se houver.
        valor_pago (float): Valor pago pelo passageiro pela compra.
        valor_desconto (float): Valor do desconto aplicado à compra, se houver. Padrão é 0.0.
        valor_total (float): Valor total da compra após aplicar descontos.
        tipo_pagamento (TipoPagamento): Tipo de pagamento utilizado na compra.
        data_compra (Optional[date]): Data em que a compra foi realizada. Padrão é None.
    """

    id_passageiro: int
    id_passagem: int
    id_bagagem: Optional[int] = None
    id_cupom: Optional[int] = None
    valor_pago: float
    valor_desconto: float
    valor_total: float
    tipo_pagamento: TipoPagamento
    data_compra: datetime