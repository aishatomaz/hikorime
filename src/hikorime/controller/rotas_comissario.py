from fastapi import APIRouter, HTTPException

from hikorime.models.enums.status_voo import StatusVoo
from hikorime.service.cadastro_voo import CadastroVooService
from hikorime.models.voo import Voo

comissario_routes = APIRouter(prefix="/voos", tags=["Gerenciamento de Voos"])

@comissario_routes.post("/cadastro")
def cadastro_voo(voo_data: Voo):
    try:
        service = CadastroVooService()

        service.save(
            **voo_data.model_dump(), status_voo=StatusVoo.DISPONIVEL
        )  # Como nao vamos retornar o atributo resultado, eu tirei ele.
        # .dict()[deprecated], foi mudado para .model_dump
        return {"status": "sucesso", "mensagem": "Voo cadastrado com sucesso!"}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=str(erro))
