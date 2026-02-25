from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from hikorime.service.voo_service import VooService
from hikorime.repository.repository_querys import RepositoryQuerys

passageiro_routes = APIRouter(prefix="/passagens", tags=["Passageiro"])


@passageiro_routes.get("/ver-voos", response_model=None)
def ver_voos():
    consulta = VisualizarVoos.get_all()

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
