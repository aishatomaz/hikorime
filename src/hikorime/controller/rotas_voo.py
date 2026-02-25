from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from hikorime.models.basemodels.bm_voo import Voo
from hikorime.service.voo_service import VooService

voo_model = Voo


class VooController:
    def __init__(self):
        self.service = VooService
        self.router = APIRouter(
            prefix=f"/{self.table_name}", tags=[self.table_name.capitalize()]
        )
