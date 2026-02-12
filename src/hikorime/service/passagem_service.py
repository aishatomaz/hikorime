from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
from hikorime.repository.repository_Passagem import RepositoryPassagem

class PassagemService(BaseService):
    def __init__(self):
        self.repo = RepositoryQuerys("passagem")

    def get_by_passageiro(self, passageiro_id: int):

        return RepositoryPassagem.get_by_passageiro(passageiro_id)