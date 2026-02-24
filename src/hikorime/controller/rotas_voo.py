from fastapi import APIRouter, HTTPException
from hikorime.service.visualizacao_de_voo import VisualizarVoos
from hikorime.models.basemodels.bm_voo import Voo

passageiro_voo_routes = APIRouter(prefix="/voo", tags=["Visualizar voo"])

@passageiro_voo_routes.get("/visualizar/voos", response_model=None)
def ver_todos_os_voos():
    consulta = VisualizarVoos.get_all()

    if not consulta:
        raise HTTPException(status_code=404, detail="Nenhum voo foi encontrado.")

    return consulta
