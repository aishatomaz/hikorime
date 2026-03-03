import re

from fastapi import APIRouter, status, Request, Form, HTTPException
from starlette.responses import RedirectResponse

from hikorime.models.basemodels.bm_login import LoginRequest
from hikorime.models.basemodels.bm_passageiro import Passageiro
from hikorime.models.basemodels.bm_funcionario import Funcionario
from hikorime.service.autenticacao_service import AutenticacaoService
from hikorime.ui.engine import HikorimeUI


registro_router = APIRouter(prefix="/registro", tags=["registro", "autenticação"])
auth_service = AutenticacaoService()


@registro_router.get("/login")
def exibir_login(request: Request):
    """
    Exibe a tela de login e coleta os dados fornecidos.
    """
    return HikorimeUI.render(
        template="registro/login.html",
        request=request,
        title="Login",
        usr=auth_service.get_current_user(request),
        data={},
    )

@registro_router.post("/login", status_code=status.HTTP_200_OK)
def login(
        request: Request,
        email : str = Form(...),
        senha : str = Form(...)
    ):
    """
    Realiza o login de um usuário (passageiro ou funcionário).
    """
    dados_login = LoginRequest(
        email=email,
        senha=senha
    )

    try:
        result: dict = auth_service.login(dados_login)
        request.session["user"] = result["usuario"] # Conectar o usuário à sessão
        return RedirectResponse(url="/", status_code=303)


    except HTTPException as e:

        input_data = {
            "email": email,
        }

        return HikorimeUI.render(
            template="registro/login.html",
            request=request,
            usr=auth_service.get_current_user(request),
            title="Falha no Login",
            err=e.detail,
            data=input_data,
        )

@registro_router.post("/logout")
def logout(request: Request):
    """
        Remove o usuário da sessão e redireciona para página inicial.
    """
    request.session.clear()

    return RedirectResponse(url="/", status_code=303)

@registro_router.get("/passageiro")
def exibir_registrar_passageiro(request: Request):
    """
    Exibe a tela de registro de passageiros e coleta os dados fornecidos.
    """
    return HikorimeUI.render(
        template="registro/passageiro.html",
        request=request,
        title="Registro de Passageiros",
        usr=auth_service.get_current_user(request),
        data={},
    )

@registro_router.post("/passageiro", status_code=status.HTTP_201_CREATED)
def registrar_passageiro(
        request: Request,
        nome: str = Form(...),
        passaporte: str = Form(...),
        cpf: str = Form(...),
        email: str = Form(...),
        senha: str = Form(...),
):
    """
    Registra um novo passageiro no sistema.
    """
    dados_passageiro = Passageiro(
        nome=nome,
        passaporte=passaporte,
        cpf=re.sub(r"\D", "", cpf),  # Romover não dígitos
        email=email,
        senha=senha,
    )

    try:
        result: dict = auth_service.registrar_passageiro(dados_passageiro)
        request.session["user"] = result["usuario"] # Conectar o usuário à sessão
        return RedirectResponse(url="/", status_code=303)

    except HTTPException as e:

        input_data = {
            "nome": nome,
            "cpf": cpf,
            "email": email,
        }

        return HikorimeUI.render(
            template="registro/passageiro.html",
            request=request,
            usr=auth_service.get_current_user(request),
            title="Falha ao Registrar Novo Passageiro",
            err=e.detail,
            data=input_data,
        )


@registro_router.get("/funcionario")
def exibir_registrar_funcionario(request: Request):
    """
    Exibe a tela de registro de funcionários e coleta os dados fornecidos.
    """
    return HikorimeUI.render(
        template="registro/funcionario.html",
        request=request,
        title="Registro de Funcionarios",
        usr=auth_service.get_current_user(request),
        data={},
    )

@registro_router.post("/funcionario", status_code=status.HTTP_201_CREATED)
def registrar_funcionario(
        request: Request,
        nome: str = Form(...),
        cpf: str = Form(...),
        cargo: str = Form(...),
        matricula: str = Form(...),
        email: str = Form(...),
        senha: str = Form(...),
    ):
    """
    Registra um novo funcionário no sistema.
    """
    dados_funcionario = Funcionario(
        nome=nome,
        cpf=re.sub(r"\D", "", cpf), # Romover não dígitos
        cargo=cargo,
        matricula=matricula,
        email=email,
        senha=senha,
    )

    try:
        result: dict = auth_service.registrar_funcionario(dados_funcionario)
        request.session["user"] = result["usuario"] # Conectar o usuário à sessão
        return RedirectResponse(url="/", status_code=303)

    except HTTPException as e:

        input_data = {
            "nome": nome,
            "cpf": cpf,
            "matricula": matricula,
            "cargo": cargo,
            "email": email,
        }

        return HikorimeUI.render(
            template="registro/funcionario.html",
            request=request,
            usr=auth_service.get_current_user(request),
            title="Falha ao Registrar Novo Funcionario",
            err=e.detail,
            data=input_data,
        )