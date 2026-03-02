from hikorime.controller.rotas_base import create_generic_router
from hikorime.service.cupom_service import CupomService
from hikorime.models.basemodels.bm_cupom import Cupom

"""A rota do comissário deve conter os gerenciamentos dos voos."""


service = CupomService()

route = create_generic_router(schema=Cupom, service=service)


@route.post("/criar")
def criar_cupom(self, cupom_data: Cupom):
    try:
        self.service.save(cupom_data)
        return {"status": "sucesso", "mensagem": "Voo cadastrado com sucesso!"}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=str(erro))
