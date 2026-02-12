from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.visualizacao_de_voo import VisualizarVoos
from hikorime.service.passagem_service import PassagemService

passageiro_routes = APIRouter(prefix="/passagens", tags=["Passageiro"])

@passageiro_routes.get("/visualizar/voos", response_model=None)
def ver_todos_os_voos():
    consulta = VisualizarVoos.dados.get_all()

    if not consulta:
        raise HTTPException(status_code=404, detail="Nenhum voo foi encontrado.")

    return consulta
