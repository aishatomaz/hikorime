from fastapi import APIRouter, HTTPException
from starlette.requests import Request

from hikorime.service.relatorio_service import RelatorioService
from hikorime.service.autenticacao_service import AutenticacaoService
from hikorime.ui.engine import HikorimeUI

relatorios_router = APIRouter(prefix="/relatorios")

relatorio_service = RelatorioService()
auth_service = AutenticacaoService()


@relatorios_router.get("/estatisticas")
def exibir_estatisticas(request: Request):
    """
    Exibe a tela com todas as estatísticas do sistema.
    Apenas funcionários podem acessar.
    """

    usr: dict = auth_service.get_current_user(request)

    if not usr or usr["tipo_usuario"] != "funcionario":
        raise HTTPException(status_code=403)

    dados = relatorio_service.todos_relatorios()

    return HikorimeUI.render(
        template="relatorios/estatisticas.html",
        request=request,
        usr=usr,
        title="Estatísticas do Sistema",
        dados=dados
    )