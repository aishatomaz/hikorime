from fastapi import HTTPException
from hikorime.controller.rotas_base import create_generic_router
from hikorime.service.compra_service import CompraService
from hikorime.models.basemodels.bm_compra import CompraPassagem

service = CompraService()

route = create_generic_router(schema=CompraPassagem, service=service)


@route.post("/finalizar-compra")
def create(compra: CompraPassagem):
    try:
        service.save(compra)
        return {"mensagem": "Compra realizada com sucesso!", "compra": compra}
    except Exception as erro:
        raise HTTPException(
            status_code=400, detail=f"Erro ao finalizar pagamento: {str(erro)}"
        )


@route.get("/historico")
def get_compras_by_passageiro_id(passageiro_id: int):
    compras = service.get_like_by_column_name("passageiro_id", passageiro_id)
    if not compras:
        raise HTTPException(
            status_code=404,
            detail="Não foram encontradas compras relacionadas à esse passageiro",
        )
    return compras
