from fastapi import APIRouter, HTTPException, status

from hikorime.models.basemodels.bm_compra import CompraPassagem
from hikorime.service.passagem_service import PassagemService

from hikorime.controller.rotas_base import create_generic_router

service = VooService()

passageiro_routes = create_generic_router(schema=Voo, service=service)


@passageiro_routes.post("/comprar", status_code=status.HTTP_201_CREATED)
def comprar_passagem(dados: CompraPassagem):
    try:
        PassagemService().save(dados)

        return {"mensagem": "Compra realizada com sucesso!", "dados": dados}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=f"Erro na compra: {str(erro)}")


@passageiro_routes.get("/visualizar")
def ver_minhas_passagens(id_passageiro: int):
    """faz a consulta das passagens vinculadas ao id do passageiro"""

    passagens = PassagemService().get_passagem_by_passageiro(id_passageiro)

    if not passagens:
        raise HTTPException(
            status_code=404, detail="Nenhuma passagem encontrada para este passageiro."
        )

    return passagens
