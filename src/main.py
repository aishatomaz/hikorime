from fastapi import FastAPI
from hikorime.controller.rotas_comissario import comissario_routes
from hikorime.controller.voo_controller import passageiro_routes
from hikorime.controller.rotas_relatorios import relatorios_routes

app = FastAPI()

app.include_router(comissario_routes)
app.include_router(passageiro_routes)
app.include_router(relatorios_routes)

