from fastapi import APIRouter, status
from hikorime.models.registro import PassageiroCreate, FuncionarioCreate, LoginRequest
from hikorime.service.registro_service import RegistroService

registro_router = APIRouter(prefix="/registro", tags=["Registro e Autenticação"])
service = RegistroService()


@registro_router.post("/login", status_code=status.HTTP_200_OK)
def login(credentials: LoginRequest):
    """
    Realiza o login de um usuário (passageiro ou funcionário).
    """
    return service.login(credentials)


@registro_router.post("/usuario/passageiro", status_code=status.HTTP_201_CREATED)
def registrar_passageiro(dados: PassageiroCreate):
    """
    Registra um novo passageiro no sistema.
    """
    return service.registrar_passageiro(dados)


@registro_router.post("/usuario/funcionario", status_code=status.HTTP_201_CREATED)
def registrar_funcionario(dados: FuncionarioCreate):
    """
    Registra um novo funcionário no sistema.
    """
    return service.registrar_funcionario(dados)
