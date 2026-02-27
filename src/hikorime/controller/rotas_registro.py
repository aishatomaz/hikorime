from fastapi import APIRouter, status, Request, Form, HTTPException
import re

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
    Exibe a tela de login e coleta os dados fornecidos.
    """
    return HikorimeUI.render(
        template="registro/login.html",
        request=request,
        title="Login",
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
    dados = LoginRequest(
        email=email,
        senha=senha
    )

    try:
        result: dict = service.login(dados)
        return HikorimeUI.render(
            template="index.html",
            request=request,
            msg=result['message'],
            usr=result['usuario'],
        )

    except HTTPException as e:

        input_data = {
            "email": email,
        }

        return HikorimeUI.render(
            template="registro/login.html",
            request=request,
            title="Falha no Login",
            err=e.detail,
            data=input_data,
        )


@registro_router.get("/passageiro")
def exibir_registrar_passageiro(request: Request):
    """
    Exibe a tela de registro de passageiros e coleta os dados fornecidos.
    """
    return HikorimeUI.render(
        template="registro/passageiro.html",
        request=request,
        title = "Registro de Passageiros",
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
    dados = Passageiro(
        nome=nome,
        passaporte=passaporte,
        cpf=re.sub(r"\D", "", cpf),  # Romover não dígitos
        email=email,
        senha=senha,
    )

    try:
        result: dict = service.registrar_passageiro(dados)
        return HikorimeUI.render(
            template="index.html",
            request=request,
            msg=result['message'],
            usr=result['usuario'],
        )

    except HTTPException as e:

        input_data = {
            "nome": nome,
            "cpf": cpf,
            "email": email,
        }

        return HikorimeUI.render(
            template="registro/passageiro.html",
            request=request,
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
    dados = Funcionario(
        nome=nome,
        cpf=re.sub(r"\D", "", cpf), # Romover não dígitos
        cargo=cargo,
        matricula=matricula,
        email=email,
        senha=senha,
    )

    try:
        result: dict = service.registrar_funcionario(dados)
        return HikorimeUI.render(
            template="index.html",
            request=request,
            msg=result['message'],
            usr=result['usuario'],
        )

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
            title="Falha ao Registrar Novo Funcionario",
            err=e.detail,
            data=input_data,
        )