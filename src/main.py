from fastapi import FastAPI
<<<<<<< HEAD
=======

>>>>>>> 741fc4069c26c338c60aaf74b4cc9cd90471b8ae
from hikorime.controller.rotas_comissario import comissario_routes
from hikorime.controller.voo_controller import passageiro_routes
from hikorime.controller.rotas_relatorios import relatorios_routes

app = FastAPI()

<<<<<<< HEAD
=======

>>>>>>> 741fc4069c26c338c60aaf74b4cc9cd90471b8ae
app.include_router(comissario_routes)
app.include_router(passageiro_routes)
app.include_router(relatorios_routes)

