from hikorime.service.base_service import BaseService
from hikorime.repository.repository_querys import RepositoryQuerys


class VisualizarVoos(BaseService):
<<<<<<< HEAD
    #classe apenas para buscas - requisições get
    def __init__(self, repositorio = RepositoryQuerys):
        self.bd = repositorio
    
    
=======
    tabela = RepositoryQuerys
    dados = tabela("voos")
>>>>>>> 8779ceeed62d9e8522b5cf4d3f278eec7879cab8
