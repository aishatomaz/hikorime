from fastapi import APIRouter, Request
from hikorime.ui.engine import HikorimeUI

base_router = APIRouter()

base_router.get("/")
def index(request: Request):
    return HikorimeUI.render("index.html", request)