from fastapi import APIRouter, HTTPException, status, Request
from fastapi.params import Form
from starlette.requests import Request
from starlette.responses import RedirectResponse
from datetime import date

from hikorime.models.basemodels.bm_passagem import Passagem
from hikorime.models.basemodels.bm_cupom import Cupom
from hikorime.models.basemodels.bm_compra import Compra

from hikorime.service.autenticacao_service import AutenticacaoService
from hikorime.service.compra_service import CompraService
from hikorime.service.cupom_service import CupomService
from hikorime.service.passagem_service import PassagemService

from hikorime.models.enums.tipo_pagamento import TipoPagamento
from hikorime.service.voo_service import VooService

from hikorime.ui.engine import HikorimeUI
from hikorime.controller.rotas_base import create_generic_router


passagens_service = PassagemService()
voo_service = VooService()
compra_service = CompraService()
cupom_service = CupomService()
auth_service = AutenticacaoService()

passagens_router = APIRouter(prefix="/passagens", tags=["passagens", "compras"])


@passagens_router.get("/minhas-passagens")
def exibir_minhas_passagens(request: Request):
    """
    Exibe o histórico de compras do passageiro.
    """
    usr = auth_service.get_current_user(request)
    if not usr:
        return RedirectResponse(url="/registro/login", status_code=303)
        
    id_passageiro = usr["id_usuario"]
    # Retornar histórico de compras (incluindo valor gasto)
    passagens:list[dict] = compra_service.get_passagens_by_passageiro_id(id_passageiro)

    return HikorimeUI.render(
        template="passagens/minhas-passagens.html",
        request=request,
        title="Minhas Passagens e Compras",
        usr=usr,
        passagens=passagens,
    )


@passagens_router.get("/comprar/{id_voo:int}")
def exibir_comprar_passagem(
    request: Request,
    id_voo: int,
):
    """
    Exibe a tela de compra de passagens.
    """
    usr = auth_service.get_current_user(request)
    if not usr:
        return RedirectResponse(url="/registro/login", status_code=303)

    voo:dict = passagens_service.get_voo_by_id(id_voo)

    return HikorimeUI.render(
        template="passagens/comprar.html",
        request=request,
        usr=usr,
        title="Comprar Passagem",
        voo=voo,
    )


@passagens_router.post("/comprar")
def comprar_passagem(
    request: Request,
    id_voo: int = Form(...),
    assento: str = Form(...),
):
    usr = auth_service.get_current_user(request)
    if not usr:
        return RedirectResponse(url="/registro/login", status_code=303)
        
    id_passageiro = usr["id_usuario"]

    dados_passagem = Passagem(
        id_passageiro=id_passageiro,
        id_voo=id_voo,
        assento=assento,
    )

    try:
        # Cria a passagem primeiro
        passagem_criada:dict = passagens_service.create_passagem(dados_passagem)
        id_passagem = passagem_criada["id"]
        
        # Redireciona para finalizar compra com detalhes
        return RedirectResponse(url=f"/passagens/finalizar-compra?id_passagem={id_passagem}", status_code=303)

    except HTTPException as e:
        voo:dict = passagens_service.get_voo_by_id(id_voo)

        return HikorimeUI.render(
            template="passagens/comprar.html",
            request=request,
            usr=usr,
            title="Falha ao Comprar Passagem",
            err=e.detail,
            voo=voo,
        )


@passagens_router.get("/finalizar-compra")
def exibir_finalizar_compra(
    request: Request,
    id_passagem: int,
):
    usr = auth_service.get_current_user(request)
    if not usr:
        return RedirectResponse(url="/registro/login", status_code=303)
        
    id_passageiro = usr["id_usuario"]
    
    # Obter detalhes da passagem e voo
    passagem_detalhada = compra_service.get_passagem_detalhada(id_passagem)
    
    # Obter cupons disponíveis para o passageiro
    cupons_disponiveis = cupom_service.get_cupons_disponiveis(id_passageiro)
    
    return HikorimeUI.render(
        template="passagens/finalizar-compra.html",
        request=request,
        title="Finalizar Compra",
        usr=usr,
        passagem=passagem_detalhada,
        cupons=cupons_disponiveis,
        tipos_pagamento=TipoPagamento.enum_to_dict(),
    )


@passagens_router.post("/finalizar-compra")
def finalizar_compra(
    request: Request,
    id_passagem: int = Form(...),
    id_cupom: int = Form(None),
    tipo_pagamento: str = Form(...),
):
    usr = auth_service.get_current_user(request)
    if not usr:
        return RedirectResponse(url="/registro/login", status_code=303)
        
    id_passageiro = usr["id_usuario"]

    try:
        dados_compra = {
            "id_passageiro": id_passageiro,
            "id_passagem": id_passagem,
            "id_cupom": id_cupom if id_cupom else None,
            "tipo_pagamento": TipoPagamento(tipo_pagamento),
        }
        
        compra_service.finalizar_compra(dados_compra)
        return RedirectResponse(url="/passagens/minhas-passagens", status_code=303)

    except HTTPException as e:
        # Recarregar dados em caso de erro
        passagem_detalhada = compra_service.get_passagem_detalhada(id_passagem)
        cupons_disponiveis = cupom_service.get_cupons_disponiveis(id_passageiro)
        
        return HikorimeUI.render(
            template="passagens/finalizar-compra.html",
            request=request,
            title="Erro ao Finalizar Compra",
            usr=usr,
            passagem=passagem_detalhada,
            cupons=cupons_disponiveis,
            tipos_pagamento=TipoPagamento.enum_to_dict(),
            err=e.detail,
        )


@passagens_router.get("/cupons")
def exibir_cupons(request: Request):
    usr = auth_service.get_current_user(request)
    if not usr:
        return RedirectResponse(url="/registro/login", status_code=303)
        
    id_passageiro = usr["id_usuario"]
    cupons = cupom_service.get_cupons_disponiveis(id_passageiro)
    
    return HikorimeUI.render(
        template="passagens/cupons.html", # Assumindo que este template existe ou será criado
        request=request,
        title="Meus Cupons",
        usr=usr,
        cupons=cupons,
    )
