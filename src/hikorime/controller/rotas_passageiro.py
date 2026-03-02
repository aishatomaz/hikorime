from fastapi import HTTPException, status
from hikorime.controller.rotas_base import create_generic_router
from hikorime.models.basemodels.bm_compra import CompraPassagem
from hikorime.models.basemodels.bm_passageiro import Passageiro
from hikorime.service.voo_service import VooService

service = VooService()

route = create_generic_router(schema=Passageiro, service=service)


@route.get("/visualizar", response_model=None)
def ve_voos(id: int):

    consulta = service.get_by_id((id))

    if not consulta:
        raise HTTPException(status_code=404, detail="Nenhum voo foi encontrado.")

    return consulta


@route.post("/finalizar", status_code=status.HTTP_201_CREATED)
def realizar_pagamento(dados: CompraPassagem):
    try:
        to_save = service.save(Passageiro)
        service.save(to_save)

        return {"mensagem": "Pagamento realizado com sucesso!", "dados": dados}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=f"Erro no pagamento: {str(erro)}")
