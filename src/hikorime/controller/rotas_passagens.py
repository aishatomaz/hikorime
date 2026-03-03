from typing import Optional

from fastapi import APIRouter, HTTPException, status
from starlette.requests import Request

from hikorime.models.basemodels.bm_compra import CompraPassagem
from hikorime.service.autenticacao_service import AutenticacaoService
from hikorime.service.compra_service import CompraService
from hikorime.service.cupom_service import CupomService
from hikorime.service.passagem_service import PassagemService
from hikorime.ui.engine import HikorimeUI


passagens_router = APIRouter(prefix="/passagens", tags=["passagens", "compras"])
passagens_service = PassagemService()
compra_service = CompraService()
cupom_service = CupomService()
auth_service = AutenticacaoService()

@passagens_router.get("/comprar")
def exibir_comprar_passagem(request: Request):
    """
    Exibe a tela de compra de passagens.
    """
    HikorimeUI.render(
        template="passgens/comprar.html",
        request=request,
        title="Comprar Passagem",
        usr=auth_service.get_current_user(request),
    )

@passagens_router.post("/comprar")
def comprar_passagem(
        request: Request,
        id_passageiro: int,
        id_voo: int,
        assento: int,
        valor_pago: float,
        id_cupom: Optional[int] = None,
    ):
    dados_passagem = CompraPassagem(
        id_passageiro=id_passageiro,
        id_voo=id_voo,
        assento=assento,
        valor_pago=valor_pago,
        id_cupom=id_cupom,
    )

    # TODO: usar service certo
    pass

@passagens_router.post("/finalizar-compra")
def finalizar_compra(request: Request):
    pass


@passagens_router.get("/minhas-passagens")
def exibir_minhas_passagens(request: Request, id_passageiro: int):
    """
    Exibe a lista de passagens associadas a um usuário.
    """
    passagens: dict = passagens_service.get_passagem_by_passageiro(id_passageiro)

    # TODO: template
    return HikorimeUI.render(
        template="passgens/minhas-passagens.html",
        request=request,
        title="Minhas Passagens",
        passages=passagens,
    )

@passagens_router.get("/cupons")
def exibir_cupons(request: Request):
    # TODO: exibir cupons disponíveis
    pass