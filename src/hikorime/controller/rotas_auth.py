from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

usuario_routes = APIRouter(prefix="/Usuários", tags=["autenticacao"])

@usuario_routes.post("/cadastro/passageiro", response_model=None)
def cadastro_passageiro(self):
    pass
@usuario_routes.post("/cadastro/funcionario", response_model=None)
def cadastro_funcionario(self):
    pass