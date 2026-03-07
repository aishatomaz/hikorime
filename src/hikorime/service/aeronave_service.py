from base_service import BaseService
from repository.repository_querys import RepositoryQuerys
from models.basemodels.bm_aeronave import Aeronave

class AeronaveService(BaseService):

    def __init__(self):
        super().__init__(RepositoryQuerys("aeronaves"))

    def cadastrar_aeronave(self, dados: Aeronave):
        """
        Cadastra uma nova aeronave usando os campos do BaseModel
        """
        return self.save(dados)
    
    def listar_aeronaves(self):
        """
        Deve exibir todas as aeronaves cadastradas no banco
        """
        return self.get_all()