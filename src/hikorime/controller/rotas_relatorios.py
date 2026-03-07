from fastapi import APIRouter, FastAPI
from hikorime.service.relatorio_service import RelatorioService

relatorios_routes = APIRouter(prefix="/relatorios", tags=["relatorios"])
relatorio_service = RelatorioService()

# Rotas básicas para os relatórios
@relatorios_routes.get("/faturamento/anual")
def relatorio_faturamento_anual():
    return relatorio_service.faturamento_anual()

@relatorios_routes.get("/faturamento/mensal")
def relatorio_faturamento_mensal():
    return relatorio_service.faturamento_mensal()

@relatorios_routes.get("/faturamento/semanal")
def relatorio_faturamento_semanal():
    return relatorio_service.faturamento_semanal()

@relatorios_routes.get("/quantidade_voos/anual")
def relatorio_quantidade_voo_anual():
    return relatorio_service.quantidade_voo_anual()

@relatorios_routes.get("/quantidade_voos/mensal")
def relatorio_quantidade_voo_mensal():
    return relatorio_service.quantidade_voo_mensal()

@relatorios_routes.get("/quantidade_voos/semanal")
def relatorio_quantidade_voo_semanal():
    return relatorio_service.quantidade_voos_semanal()

@relatorios_routes.get("/passageiros_que_mais_compraram_passagens")
def relatorio_passageiros_que_mais_compraram_passagens():
    return relatorio_service.passageiro_comprou_mais_passagens()

@relatorios_routes.get("/todos_relatorios")
def relatorio_todos_relatorios():
    return relatorio_service.todos_relatorios()

app = FastAPI()
app.include_router(relatorios_routes)