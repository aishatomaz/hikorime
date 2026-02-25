from fastapi import APIRouter, HTTPException
from hikorime.service.compra_service import CompraService
from hikorime.models.basemodels.bm_compra import CompraPassagem

pagamento_router = APIRouter(prefix="/compras", tags=["Compras"])

service = CompraService()


@pagamento_router.post("/finalizar-compra")
def finalizar_compra(compra: CompraPassagem):
    try:
        service.save(compra)
        return {"mensagem": "Compra realizada com sucesso!", "compra": compra}
    except Exception as erro:
        raise HTTPException(
            status_code=400, detail=f"Erro ao finalizar pagamento: {str(erro)}"
        )


@pagamento_router.get("/historico_de_compras")
def ver_minhas_compras(passageiro_id: int):
    compras = service.visualizar_compras(passageiro_id)
    if not compras:
        raise HTTPException(
            status_code=404,
            detail="Não foram encontradas compras relacionadas à esse passageiro",
        )
    return compras
