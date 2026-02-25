from fastapi import APIRouter, HTTPException

from hikorime.service.cupom_service import CupomService
from hikorime.models.basemodels.bm_cupom import Cupom

"""A rota do comissário deve conter os gerenciamentos dos voos."""

comissario_routes = APIRouter(prefix="/cupom", tags=[""])

service = CupomService()


@comissario_routes.post("/cadastro")
def Criar_Cupom(cupom_data: Cupom):
    try:
        service.save(cupom_data)
        return {"status": "sucesso", "mensagem": "Voo cadastrado com sucesso!"}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=str(erro))
