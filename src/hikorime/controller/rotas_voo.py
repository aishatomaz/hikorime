from hikorime.controller.rotas_base import create_generic_router
from hikorime.models.basemodels.bm_voo import Voo
from hikorime.service.voo_service import VooService

service = VooService()

route = create_generic_router(schema=Voo, service=service)
