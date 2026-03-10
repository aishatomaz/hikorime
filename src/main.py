from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles
from pathlib import Path

#from hikorime.controller.rotas_comissario import comissario_routes
#from hikorime.controller.rotas_voo import passageiro_routes
#from hikorime.controller.rotas_relatorios import relatorios_routes
from hikorime.controller.root import base_router
from hikorime.controller.rotas_registro import registro_router
from hikorime.controller.rotas_voos import voos_router
from hikorime.controller.rotas_passagens import passagens_router
from hikorime.controller.rotas_relatorios import relatorios_router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

app.mount(
    app=StaticFiles(directory=BASE_DIR / "hikorime" / "ui" / "static"),
    path="/static",
    name="static"
)

app.add_middleware(
    SessionMiddleware,
    secret_key="super-secret-key"
)
app.include_router(base_router)
app.include_router(registro_router)
app.include_router(voos_router)
app.include_router(passagens_router)
app.include_router(relatorios_router)
