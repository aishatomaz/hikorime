from fastapi import HTTPException
from hikorime.models.basemodels.bm_cupom import Cupom
from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
from hikorime.repository.repository_compra import RepositoryCompra


class CupomService(BaseService):
    events_repository: RepositoryCompra

    def __init__(self):
        self.repo = RepositoryQuerys("cupons")

    def create_cupom(self, cupom_data: dict):
        """
        cria um novo cupom

        args:
            cupom_data: dicionario com os dados do cumpom a ser salvo.

        returns:
            dict: dados do cupom salvo (id gerado, etc.)
        """

        try:
            cupom = Cupom(**cupom_data)
            return self.save(cupom)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao criar voo: {str(e)}")
