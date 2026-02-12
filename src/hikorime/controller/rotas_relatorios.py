from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

relatorios_routes = APIRouter(prefix="/Relatorios", tags=["relatorios"])

# deignada a Gabriel
@relatorios_routes.get("/", response_model=None)
def relatorio():
    pass
