from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date, time
from hikorime.service.cadastro_voo import CadastroVooService
from hikorime.repository.repository_querys import RepositoryQuerys

comissario_routes = APIRouter(prefix="/voos", tags=["Gerenciamento de Voos"])

class VooModelo(BaseModel):
    data_saida: date
    data_cheg: date
    hora_saida: time
    hora_chega: time
    local_saida: str
    destino: str
    id_piloto: int
    aviao: int
    quant_vagas: int

@comissario_routes.post("/cadastro")
def cadastro_voo(voo_data: VooModelo):
    try:
        repo = RepositoryQuerys(table_name="voos")
        service = CadastroVooService(repo)
        
        resultado = service.save(
            **voo_data.dict(),
            status_voo="DISPONIVEL" 
        )
        return {"status": "sucesso", "mensagem": "Voo cadastrado com sucesso!"}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=str(erro))