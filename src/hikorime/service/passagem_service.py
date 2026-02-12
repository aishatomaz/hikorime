from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
<<<<<<< HEAD

'''Salva os de passagem no Banco de dados.'''
=======
from hikorime.repository.repository_Passagem import RepositoryPassagem

>>>>>>> 741fc4069c26c338c60aaf74b4cc9cd90471b8ae
class PassagemService(BaseService):
    def __init__(self):
        self.repo = RepositoryQuerys("passagem")

    def get_by_passageiro(self, passageiro_id: int):

        return RepositoryPassagem.get_by_passageiro(passageiro_id)