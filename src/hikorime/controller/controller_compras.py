from fastapi import APIRouter, HTTPException, status
from hikorime.service.compra_service import CompraService
from hikorime.models.compra import Compra

pagamento_router = APIRouter(prefix="/compras", tags =["Compras"])

@pagamento_router.post("/finalizar_compra")
def finalizar_compra(compra: Compra):
    try:
        service = CompraService()
        service.save()
        return {"mensagem": "Compra realizada com sucesso!", "compra": compra}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=f"Erro ao finalizar pagamento: {str(erro)}")
    
@pagamento_router.get("/ver_historico_de_compras")
def ver_minhas_compras(passageiro_id: int):
    service = CompraService()
    compras = service.visualizar_compras(passageiro_id)
    if not compras:
        raise HTTPException(status_code=404, detail="Não foram encontradas compras relacionadas à esse passageiro")
    return compras