from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

'''A API mostra os relatórios do sistema. O contúdo dos relatórios ainda não foi completamente definido.'''

relatorios_routes = APIRouter(prefix="/Relatorios", tags=["relatorios"])

@relatorios_routes.get("/", response_model=None)
def relatorio():
    pass
@relatorios_routes.get("/", response_model=None)
def relatorio():
    pass