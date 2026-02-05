from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from service.visualizacao_de_voo import VisualizarVoos

get_routes = APIRouter(prefix="/voos", tags=["voos"])

@get_routes.get("/visualizar/voos", response_model=None)
def ver_todos_os_voos():
    consulta = VisualizarVoos.get_all(table_name="voos")

    if not consulta:
        raise HTTPException(status_code=404, detail="Nenhum voo foi encontrado.")
        
    return consulta
