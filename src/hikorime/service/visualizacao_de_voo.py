from hikorime.service.base_service import BaseService
from hikorime.repository.repository_querys import RepositoryQuerys


class VisualizarVoos(BaseService):
    #classe apenas para buscas - requisições get
    def __init__(self, repositorio = RepositoryQuerys):
        self.bd = repositorio
    
    