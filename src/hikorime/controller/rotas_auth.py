from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from datetime import date
from hikorime.repository.repository_querys import RepositoryQuerys

usuario_routes = APIRouter(prefix="/usuarios", tags=["Autenticação"])

#modelos de entrada
class CadastroPassageiro(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    data_nascimento: date

class CadastroFuncionario(BaseModel):
    nome: str
    matricula: str
    cargo: str

#rotas de cadastro

@usuario_routes.post("/cadastro/passageiro", status_code=status.HTTP_201_CREATED)
def cadastro_passageiro(dados: CadastroPassageiro):
    try:
        #salvamento dos dados inseridos pelo usuário no banco
        repo = RepositoryQuerys(table_name="passageiros")
        repo.save(**dados.dict()) 
        return {"mensagem": "Passageiro cadastrado com sucesso!"}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=str(erro))

@usuario_routes.post("/cadastro/funcionario", status_code=status.HTTP_201_CREATED)
def cadastro_funcionario(dados: CadastroFuncionario):
    try:
        repo = RepositoryQuerys(table_name="funcionarios")
        repo.save(**dados.dict())
        return {"mensagem": "Funcionário cadastrado com sucesso!"}
    except Exception as erro:
        raise HTTPException(status_code=400, detail=str(erro))