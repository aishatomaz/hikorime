from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from datetime import date, time
from service.cadastro_voo_bd import CadastrarVoo

comissario_routes = APIRouter(prefix="/Usuários", tags=["autenticacao"])

@comissario_routes.post("/cadastro/voo", response_model=None)

class CadastroVoo(BaseModel):
    data_saida: date
    data_cheg: date 
    hora_saida: time
    hora_chega: time
    local_saida: str 
    destino: str
    id_piloto: int 
    aviao: int
    quant_vagas: int

def cadastro_voo(voo: CadastroVoo):
    try:
        CadastrarVoo = CadastrarVoo(
            self.data_saida,
            self.data_cheg,
            self.hora_saida,
            self.hora_chega,
            self.local_saida, 
            self.destino, 
            self.id_piloto, 
            self.aviao, 
            self.quant_vagas

        )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))