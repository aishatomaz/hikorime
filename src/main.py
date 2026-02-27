from fastapi import FastAPI, Request

#from hikorime.controller.rotas_comissario import comissario_routes
#from hikorime.controller.rotas_voo import passageiro_routes
#from hikorime.controller.rotas_relatorios import relatorios_routes
from hikorime.controller.rotas_registro import *
app = FastAPI()

#app.include_router(comissario_routes)
#app.include_router(passageiro_routes)
#app.include_router(relatorios_routes)
app.include_router(registro_router)
