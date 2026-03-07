from fastapi import APIRouter, HTTPException, status, Request
from fastapi.params import Form
from starlette.requests import Request
from starlette.responses import RedirectResponse

from hikorime.models.basemodels.bm_passagem import Passagem
from hikorime.models.basemodels.bm_cupom import Cupom
from hikorime.models.basemodels.bm_compra import Compra

from hikorime.service.autenticacao_service import AutenticacaoService
from hikorime.service.compra_service import CompraService
from hikorime.service.cupom_service import CupomService
from hikorime.service.passagem_service import PassagemService

from hikorime.models.enums.tipo_pagamento import TipoPagamento

from hikorime.ui.engine import HikorimeUI
from hikorime.controller.rotas_base import create_generic_router


passagens_service = PassagemService()
compra_service = CompraService()
cupom_service = CupomService()
auth_service = AutenticacaoService()

passagens_router = APIRouter(prefix="/passagens", tags=["passagens", "compras"])


@passagens_router.get("/minhas-passagens")
def exibir_minhas_passagens(request: Request):
    """
    Exibe a lista de passagens associadas a um usuário.
    """
    #passagens: dict = passagens_service.get_passagem_by_passageiro(id_passageiro)
    # TODO: RETORNAR INFO DE PASSAGEM + VOO + CUPOM

    return HikorimeUI.render(
        template="passagens/minhas-passagens.html",
        request=request,
        title="Minhas Passagens",
        usr=auth_service.get_current_user(request),
        #passagens=passagens,
        # TODO: RETORNAR INFO DE PASSAGEM + VOO + CUPOM
    )


@passagens_router.get("/comprar/{id_voo:int}")
def exibir_comprar_passagem(
    request: Request,
    id_voo: int,
):
    """
    Exibe a tela de compra de passagens.
    """
    return HikorimeUI.render(
        template="passagens/comprar.html",
        request=request,
        usr=auth_service.get_current_user(request),
        title="Comprar Passagem",
        id_voo=id_voo,
    )


@passagens_router.post("/comprar")
def comprar_passagem(
    request: Request,
    id_voo: int = Form(...),
    assento: int = Form(...),
):

    usr = auth_service.get_current_user(request)
    id_passageiro = usr["id_usuario"]

    dados_passagem = Passagem(
        id_passageiro=id_passageiro,
        id_voo=id_voo,
        assento=assento,
    )

    try:
        passagem: dict = passagens_service.create_passagem(dados_passagem)

        return HikorimeUI.render(
            template="passagens/finalizar-compra.html",
            request=request,
            title="Finalizar Compra",
            usr=auth_service.get_current_user(request),
            passagem=passagem,
        )

    except HTTPException as e:
        return HikorimeUI.render(
            template="passagens/comprar.html",
            request=request,
            usr=auth_service.get_current_user(request),
            title="Falha ao Comprar Passagem",
            err=e.detail,
        )


@passagens_router.get("/finalizar-compra")
def exibir_finalizar_compra(
    request: Request,
    passagem: dict,
):
    return HikorimeUI.render(
        template="passagens/finalizar-compra.html",
        request=request,
        title="Finalizar Compra",
        usr=auth_service.get_current_user(request),
        passagem=passagem,
    )


@passagens_router.post("/finalizar-compra")
def finalizar_compra(
    request: Request,
    passagem: dict,
    cupom: dict,
):

    # TODO: CALCULAR VALOR PASSAGEM CONSIDERANDO O CUPOM
    valor_pago: float = 0.0
    tipo_pagamento = TipoPagamento(passagem["tipo_pagamento"])

    dados_compra = Compra(
        id_passagem=passagem["id_passagem"],
        id_cupom=cupom["id_cupom"],
        valor_pago=valor_pago,
        id_bagagem=0,
        tipo_pagamento=tipo_pagamento,
    )

    try:
        compra_service.save(dados_compra)  # TODO
        return RedirectResponse(url="passagens/minhas-passagens", status_code=303)

    except HTTPException as e:
        return HikorimeUI.render(
            template="passagens/finalizar-compra.html",
            request=request,
            title="Erro ao Finalizar Compra",
            usr=auth_service.get_current_user(request),
            detail=e.detail,
        )


@passagens_router.get("/cupons")
def exibir_cupons(request: Request):
    cupons = cupom_service.get_all()
    pass

