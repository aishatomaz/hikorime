from datetime import datetime

from fastapi import APIRouter, HTTPException, status, Form
from starlette.requests import Request

from hikorime.models.basemodels.bm_voo import Voo
from hikorime.service.autenticacao_service import AutenticacaoService
from hikorime.service.voo_service import VooService
from hikorime.ui.engine import HikorimeUI


voos_router = APIRouter(prefix="/voos", tags=["voos"])
voos_service = VooService()
auth_service = AutenticacaoService()


@voos_router.get("/disponiveis")
def exibir_voos_disponiveis(
        request: Request,
    ):
    """
    Exibe a lista de voos disponiveis.
    """
    # TODO:  voos_service.get_all()
    pass


# Somente para funcionários
@voos_router.get("/cadastrar")
def exibir_cadastrar_voo(
        request: Request,
    ):
    """
    Exibe a tela de cadastro de vôos (usado por funcionários)
    """
    # TODO: aeronave.get_all(), render()
    pass

# Somente para funcionários
@voos_router.get("/cadastrar")
def cadastrar_voo(
        request: Request,
        id_aeronave: int = Form(...),
        data_hora_partida: datetime = Form(...),
        data_hora_chegada: datetime = Form(...),
        local_origem: str = Form(...),
        local_destino: str = Form(...),
        terminal: str = Form(...),
        portao_embarque: str = Form(...),
    ):
    """
    Cadastra um voo no sistema (usado por funcionários)
    """

    dados_voo = Voo(
        id_aeronave=id_aeronave,
        data_hora_partida=data_hora_partida,
        data_hora_chegada=data_hora_chegada,
        local_origem=local_origem,
        local_destino=local_destino,
        terminal=terminal,
        portao_embarque=portao_embarque,
    )

    try:
        result: dict = voos_service.save(dados_voo)
        # TODO: render()


    except HTTPException as e:

        input_data = {
            "data_hora_partida": data_hora_partida,
            "data_hora_chegada": data_hora_chegada,
            "local_origem": local_origem,
            "local_destino": local_destino,
            "terminal": terminal,
            "portao_embarque": portao_embarque,
        }

        HikorimeUI.render(
            template="voos/cadastrar.html",
            request=request,
            usr=auth_service.get_current_user(request),
            title="Falha ao Cadastrar Voo",
            err=e.detail,
            data=input_data,
        )
