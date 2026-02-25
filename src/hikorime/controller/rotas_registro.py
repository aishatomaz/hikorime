from fastapi import APIRouter, status
from hikorime.models.basemodels.bm_login import LoginRequest
from hikorime.models.basemodels.bm_passageiro import Passageiro
from hikorime.models.basemodels.bm_funcionario import Funcionario
from hikorime.service.autenticacao import Autenticacao

registro_router = APIRouter(prefix="/registro", tags=["Registro e Autenticação"])
service = Autenticacao()


@registro_router.post("/login", status_code=status.HTTP_200_OK)
def login(credentials: LoginRequest):
    """
    Realiza o login de um usuário (passageiro ou funcionário).
    """
    return service.login(credentials)


@registro_router.post("/passageiro", status_code=status.HTTP_201_CREATED)
def registrar_passageiro(dados: Passageiro):
    """
    Registra um novo passageiro no sistema.
    """
    return service.registrar_passageiro(dados)


@registro_router.post("/funcionario", status_code=status.HTTP_201_CREATED)
def registrar_funcionario(dados: Funcionario):
    """
    Registra um novo funcionário no sistema.
    """
    return service.registrar_funcionario(dados)
