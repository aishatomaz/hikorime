from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

passageiro_routes = APIRouter(prefix="/Usuários", tags=["autenticacao"])

class VendaPassagem(BaseModel):
    assento: int
    voo: int

@passageiro_routes.post("/comprar/passagem/", response_model=None)
def comprar_passagem(passagem: VendaPassagem):
    try:
        VendaPassagem = #classe de venda passagem(
        self.assento,
        self.voo)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))