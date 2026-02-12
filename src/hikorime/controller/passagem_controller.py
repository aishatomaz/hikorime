from fastapi import APIRouter, HTTPException, status

from hikorime.controller.voo_controller import CompraPassagem
from hikorime.service.passagem_service import PassagemService


passageiro_routes = APIRouter(prefix="/passagens", tags=["Passageiro"])

@passageiro_routes.post("/comprar", status_code=status.HTTP_201_CREATED)
def comprar_passagem(dados: CompraPassagem):
    try:
        # salva a venda da passagem na tabela de passagens vendidas
        service = PassagemService()
        service.save()

        return {"mensagem": "Compra realizada com sucesso!", "dados": dados}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=f"Erro na compra: {str(erro)}")


@passageiro_routes.get("/minhas_passagens/")
def ver_minhas_passagens(id_passageiro: int):
    # faz a consulta das passagens vinculadas ao id do passageiro

    service = PassagemService()
    passagens = service.get_by_passageiro(id_passageiro)

    if not passagens:
        raise HTTPException(
            status_code=404, detail="Nenhuma passagem encontrada para este passageiro."
        )

    return passagens
