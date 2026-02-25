from fastapi.exceptions import HTTPException
from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
from hikorime.models.basemodels.bm_voo import Voo


class VooService(BaseService):
    def __init__(self):
        self.repo = RepositoryQuerys("voo")

    def create_voo(self, voo_data: dict):
        """
        cria um novo voo, usando o modelo genérico de save.

        args:
            voo_data: dicionário com os dados do voo a ser salvo.

        returns:
            dict: dados do voo salvo (id gerado, etc.)
        """
        try:
            voo = Voo(**voo_data)
            return self.save(voo)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao criar voo: {str(e)}")
