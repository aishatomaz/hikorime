from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from repository.repository_querys import RepositoryQuerys

passageiro_routes = APIRouter(prefix="/passagens", tags=["Passageiro"])

class CompraPassagem(BaseModel):
    assento: int
    id_voo: int
    id_passageiro: int
    valor_pago: float

@passageiro_routes.post("/comprar", status_code=status.HTTP_201_CREATED)
def comprar_passagem(dados: CompraPassagem):
    try:
        #salva a venda da passagem na tabela de passagens vendidas
        repo = RepositoryQuerys(table_name="passagens_vendidas")
        repo.save(**dados.dict())
        
        return {"mensagem": "Compra realizada com sucesso!", "dados": dados}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=f"Erro na compra: {str(erro)}")

@passageiro_routes.get("/meus-voos/{id_passageiro}")
def ver_minhas_passagens(id_passageiro: int):
    #faz a consulta das passagens vinculadas ao id do passageiro
    repo = RepositoryQuerys(table_name="passagens_vendidas")
    passagens = repo.get_by_column_name("id_passageiro", id_passageiro)
    
    if not passagens:
        raise HTTPException(status_code=404, detail="Nenhuma passagem encontrada para este passageiro.")
        
    return passagens
