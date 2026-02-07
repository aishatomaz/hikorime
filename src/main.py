from fastapi import FastAPI

app = FastAPI()

from hikorime.controller.rotas_auth import usuario_routes
from hikorime.controller.rotas_comissario import comissario_routes
from hikorime.controller.rotas_passageiro import passageiro_routes
from hikorime.controller.rotas_relatorios import relatorios_routes

app.include_router(usuario_routes)
app.include_router(comissario_routes)
app.include_router(passageiro_routes)
app.include_router(relatorios_routes)
