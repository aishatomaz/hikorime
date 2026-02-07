from hikorime.service.base_service import BaseService
from hikorime.repository.repositoryQuerys import repositoryQuerys


class VisualizarVoos(BaseService):
    tabela = repositoryQuerys
    dados = tabela("voos")
