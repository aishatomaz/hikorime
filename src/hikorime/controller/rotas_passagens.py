from typing import Optional

from fastapi import APIRouter, HTTPException, status, Request
from starlette.requests import Request, RedirectResponse

from hikorime.models.basemodels.bm_passagem import CompraPassagem
from hikorime.models.basemodels.bm_passagem import CompraPassagem
from hikorime.models.basemodels.bm_cupom import Cupom
from hikorime.service.autenticacao_service import AutenticacaoService
from hikorime.service.compra_service import CompraService
from hikorime.service.cupom_service import CupomService
from hikorime.service.passagem_service import PassagemService
from hikorime.ui.engine import HikorimeUI
from hikorime.controller.rotas_base import create_generic_router


#passagens_router = APIRouter(prefix="/passagens", tags=["passagens", "compras"])
passagens_service = PassagemService()
compra_service = CompraService()
cupom_service = CupomService()
auth_service = AutenticacaoService()

passagens_router = create_generic_router(schema=CompraPassagem, service=passagens_service)
compra_router = create_generic_router(schema=CompraPassagem, service=CompraService)
cupom_router = create_generic_router(schema=Cupom, service = CupomService)

@passagens_router.get("/comprar")
def exibir_comprar_passagem(request: Request):
    """
    Exibe a tela de compra de passagens.
    """
    HikorimeUI.render(
        template="passagens/comprar.html",
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
        # valor_pago: float,
        # id_cupom: Optional[int] = None, TODO: atualizar UI
    ):
    dados_passagem = CompraPassagem(
        id_passageiro=id_passageiro,
        id_voo=id_voo,
        assento=assento,
        #valor_pago=valor_pago, TODO:  atualizar UI
        #id_cupom=id_cupom,
    )

    try:
        result: dict = passagens_service.create_passagem(dados_passagem)

        return RedirectResponse(url="/", status_code=303)
    
    except HTTPException as e:
        return HikorimeUI.render(
            template="passagens/comprar.html",
            request=request,
            usr=auth_service.get_current_user(request),
            title="Falha ao Comprar Passagem",
            err=e.detail,
        )

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