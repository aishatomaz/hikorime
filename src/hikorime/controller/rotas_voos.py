import re
from datetime import datetime

from fastapi import APIRouter, HTTPException, Form
from starlette.requests import Request
from starlette.responses import RedirectResponse

from hikorime.models.basemodels.bm_aeronave import Aeronave
from hikorime.models.basemodels.bm_voo import Voo
from hikorime.service.aeronave_service import AeronaveService
from hikorime.service.autenticacao_service import AutenticacaoService
from hikorime.service.voo_service import VooService
from hikorime.ui.engine import HikorimeUI


voos_service = VooService()
aeronave_service = AeronaveService()
auth_service = AutenticacaoService()

voos_router = APIRouter(prefix="/voos")

@voos_router.get("/disponiveis")
def exibir_voos_disponiveis(
        request: Request,
    ):
    """
    Exibe a lista de voos disponíveis.
    """
    voos: list[dict] = voos_service.get_all()
    # TODO: CONSERTAR ERRO NO SERVICE

    return HikorimeUI.render(
        template="voos/disponiveis.html",
        request=request,
        title="Voos Disponiveis",
        usr=auth_service.get_current_user(request),
        voos=voos,
        # TODO: CONSERTAR ERRO NO SERVICE
    )


# Somente para funcionários
@voos_router.get("/cadastrar")
def exibir_cadastrar_voo(
        request: Request,
    ):
    """
    Exibe a tela de cadastro de voos (usado por funcionários).
    """

    aeronaves:list[dict] = aeronave_service.listar_aeronaves()

    return HikorimeUI.render(
        template="voos/cadastrar.html",
        request=request,
        title="Cadastrar Voo",
        usr=auth_service.get_current_user(request),
        aeronaves=aeronaves,
        data={},
    )

# Somente para funcionários
@voos_router.post("/cadastrar")
def cadastrar_voo(
        request: Request,
        id_aeronave: int = Form(...),
        data_hora_partida: str = Form(...),
        data_hora_chegada: str = Form(...),
        local_origem: str = Form(...),
        local_destino: str = Form(...),
        terminal: str = Form(...),
        portao_embarque: str = Form(...),
        valor_base_passagem: str = Form(...),
    ):
    """
    Cadastra um voo no sistema (usado por funcionários).
    """
    usr: dict = auth_service.get_current_user(request)

    if not usr or usr["tipo_usuario"] != "funcionario":
        raise HTTPException(status_code=403)

    # Remover não dígitos e converter para float,
    # necessário devido ao RegEx usado para formatar valores monetários
    valor_base_passagem:float = float(
        re.sub(pattern=r"\D", repl="",string=valor_base_passagem)
    ) / 100 # centavo para real

    dados_voo = Voo(
        id_aeronave=id_aeronave,
        data_hora_partida=datetime.fromisoformat(data_hora_partida),
        data_hora_chegada=datetime.fromisoformat(data_hora_chegada),
        local_origem=local_origem,
        local_destino=local_destino,
        terminal=terminal,
        portao_embarque=portao_embarque,
        valor_base_passagem=valor_base_passagem
    )
    # TODO: CHECAR SE DATA/HORA-CHEGADA <= DATA/HORA-PARTIDA
    # TODO: CHECAR ANO INFORMADO

    try:
        result: dict = voos_service.save(dados_voo)
        return HikorimeUI.render(
            template="index.html",
            request=request,
            usr=auth_service.get_current_user(request),
            #msg=result.msg
            # TODO: RETURN DA MSG DE SUCESSO
        )


    except HTTPException as e:

        input_data = {
            "data_hora_partida": data_hora_partida,
            "data_hora_chegada": data_hora_chegada,
            "local_origem": local_origem,
            "local_destino": local_destino,
            "terminal": terminal,
            "portao_embarque": portao_embarque,
        }

        return HikorimeUI.render(
            template="voos/cadastrar.html",
            request=request,
            usr=auth_service.get_current_user(request),
            title="Falha ao Cadastrar Voo",
            err=e.detail,
            data=input_data,
        )

# Somente para funcionários
@voos_router.get("/cadastrar-aeronave")
def exibir_cadastrar_aeronave(request: Request):
    """
    Exibe a tela de cadastro de aeronaves (usado por funcionários).
    """
    usr: dict = auth_service.get_current_user(request)

    if not usr or usr["tipo_usuario"] != "funcionario":
        raise HTTPException(status_code=403)

    return HikorimeUI.render(
        template="voos/cadastrar-aeronave.html",
        request=request,
        usr=auth_service.get_current_user(request),
        title="Cadastrar Aeronave",
        data={},
    )

# Somente para funcionários
@voos_router.post("/cadastrar-aeronave")
def cadastrar_aeronave(
        request: Request,
        modelo: str = Form(...),
        total_assentos: int = Form(...),
    ):
    """
    Cadastra uma aeronave no sistema (usado por funcionários).
    """
    dados_aeronave = Aeronave(
        modelo=modelo,
        total_assentos=total_assentos,
    )

    try:
        aeronave_service.cadastrar_aeronave(dados_aeronave)
        return RedirectResponse(url="/", status_code=303)

    except HTTPException as e:

        input_data = {
            "modelo": modelo,
            "total_assentos": total_assentos,
        }

        return HikorimeUI.render(
            template="voos/cadastrar-aeronave.html",
            request=request,
            usr=auth_service.get_current_user(request),
            title="Cadastrar Aeronave",
            err=e.detail,
            data=input_data,
        )