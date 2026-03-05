from fastapi import APIRouter, Request
from hikorime.ui.engine import HikorimeUI
from hikorime.service.autenticacao_service import AutenticacaoService

auth_service = AutenticacaoService()
base_router = APIRouter()

@base_router.get("/")
def index(request: Request):
    return HikorimeUI.render(
        template="index.html",
        request=request,
        usr=auth_service.get_current_user(request),
    )