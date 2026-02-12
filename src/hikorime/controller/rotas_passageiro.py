from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from hikorime.service.visualizacao_de_voo import VisualizarVoos
from hikorime.repository.repository_querys import RepositoryQuerys

passageiro_routes = APIRouter(prefix="/passagens", tags=["Passageiro"])

class CompraPassagem(BaseModel):
    assento: int
    id_voo: int
    id_passageiro: int
    valor_pago: float

@passageiro_routes.post("/comprar", status_code=status.HTTP_201_CREATED)
def comprar_passagem(dados: CompraPassagem):
    try:
        # salva a venda da passagem na tabela de passagens vendidas
        repo = RepositoryQuerys(table_name="passagens_vendidas")
        repo.save(**dados.dict())

        return {"mensagem": "Compra realizada com sucesso!", "dados": dados}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=f"Erro na compra: {str(erro)}")


@passageiro_routes.get("/meus-voos/")
def ver_minhas_passagens(id_passageiro: int):
    # faz a consulta das passagens vinculadas ao id do passageiro
    repo = RepositoryQuerys(table_name="passagens_vendidas")
    passagens = repo.get_by_column_name("id_passageiro", id_passageiro)

    if not passagens:
        raise HTTPException(
            status_code=404, detail="Nenhuma passagem encontrada para este passageiro."
        )

    return passagens


@passageiro_routes.get("/visualizar/voos", response_model=None)
def ver_todos_os_voos():
    consulta = VisualizarVoos.dados.get_all()

    if not consulta:
        raise HTTPException(status_code=404, detail="Nenhum voo foi encontrado.")

    return consulta

@passageiro_routes.post("/finalizar_compra", status_code=status.HTTP_201_CREATED)
def realizar_pagamento(dados: CompraPassagem):
    try:
        repo = RepositoryQuerys(table_name="compra")
        repo.save(**dados.dict())

        return {"mensagem": "Pagamento realizado com sucesso!", "dados": dados}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=f"Erro no pagamento: {str(erro)}")
