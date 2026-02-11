from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

relatorios_routes = APIRouter(prefix="/Relatorios", tags=["relatorios"])

@relatorios_routes.get("/", response_model=None)
def relatorio():
    pass
@relatorios_routes.get("/", response_model=None)
def relatorio():
    pass