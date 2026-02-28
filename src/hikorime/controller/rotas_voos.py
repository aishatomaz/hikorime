from fastapi import APIRouter, HTTPException, status
from starlette.requests import Request

from hikorime.models.basemodels.bm_voo import Voo
from hikorime.service.voo_service import VooService
from hikorime.ui.engine import HikorimeUI


voos_router = APIRouter(prefix="/voos", tags=["voos"])
voos_service = VooService()


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
def cadastrar_voo(
        request: Request,
        data_hora_partida: datetime,
        data_hora_chegada: datetime,
        local_origem: str,
        local_destino: str,
        assentos_ocupados: int,
    ):

    """
    Cadastra um voo no sistema (usado por funcionários)
    """

    dados = Voo(
        data_hora_partida=data_hora_partida,
        data_hora_chegada=data_hora_chegada,
        local_origem=local_origem,
        local_destino=local_destino,
        assentos_ocupados=assentos_ocupados,
        valor_passagens=0, # TODO: remover
    )

    try:
        result: dict = voos_service.save(dados)
        # TODO: render()


    except HTTPException as e:

        input_data = {
            "data_hora_partida": data_hora_partida,
            "data_hora_chegada": data_hora_chegada,
            "local_origem": local_origem,
            "local_destino": local_destino,
            "assentos_ocupados": assentos_ocupados,
        }

        HikorimeUI.render(
            template="voos/cadastrar.html",
            request=request,
            title="Falha ao Cadastrar Voo",
            err=e.detail,
            data=input_data,
        )
