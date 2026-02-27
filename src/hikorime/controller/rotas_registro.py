from fastapi import APIRouter, status, Request, Form
from starlette.responses import RedirectResponse

from hikorime.models.basemodels.bm_login import LoginRequest
from hikorime.models.basemodels.bm_passageiro import Passageiro
from hikorime.models.basemodels.bm_funcionario import Funcionario
from hikorime.service.autenticacao import Autenticacao

from hikorime.ui.engine import HikorimeUI

registro_router = APIRouter(prefix="/registro", tags=["Registro e Autenticação"])
service = Autenticacao()

@registro_router.get("/login")
def exibir_login(request: Request):
    """
    Exibe a tela de login.
    """
    return HikorimeUI.render("registro/login.html", request)


@registro_router.post("/login", status_code=status.HTTP_200_OK)
def login(request: Request,
        email : str = Form(...),
        senha : str = Form(...)
    ):
    """
    Realiza o login de um usuário (passageiro ou funcionário).
    """

    # TODO: LoginResquest deve receber ``tipo`` (tipo de usuário)

    credentials = LoginRequest(email=email, senha=senha)
    resultado = service.login(credentials)

    if not resultado:
        return HikorimeUI.render(
            "registro/login.html",
            request,
            email=email,
            erro="Credenciais Inválidas!"
        )

    return RedirectResponse("/homepage")


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
