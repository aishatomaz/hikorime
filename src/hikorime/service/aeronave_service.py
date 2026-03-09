from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.models.basemodels.bm_aeronave import Aeronave
from fastapi.exceptions import HTTPException
from hikorime.service.base_service import BaseService


class AeronaveService(BaseService):
    def __init__(self):
        self.repo = RepositoryQuerys(table_name="aeronaves", id_column="id_aeronave")

    def cadastrar_aeronave(self, aeronave: Aeronave):
        """
        Cadastra uma nova aeronave usando os campos do BaseModel
        """
        try:
            return self.save(aeronave)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao criar voo: {str(e)}")

    def listar_aeronaves(self):
        """
        Deve exibir todas as aeronaves cadastradas no banco
        """
        return self.get_all()
