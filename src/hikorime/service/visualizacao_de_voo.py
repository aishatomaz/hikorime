from hikorime.service.base_service import BaseService
from hikorime.repository.repository_querys import RepositoryQuerys

'''Salva os valores na tabela de voos.'''
class VisualizarVoos(BaseService):
    def __init__(self):
        self.repository = RepositoryQuerys("voos")
