from fastapi import APIRouter, HTTPException
from hikorime.service.visualizacao_de_voo import VisualizarVoos

passageiro_routes = APIRouter(prefix="/voo", tags=["Passageiro"])

@passageiro_routes.get("/visualizar", response_model=None)
def ver_todos_os_voos():
    consulta = VisualizarVoos.get_all()

    if not consulta:
        raise HTTPException(status_code=404, detail="Nenhum voo foi encontrado.")

    return consulta
