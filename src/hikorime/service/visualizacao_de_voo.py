from hikorime.service.base_service import BaseService
from hikorime.repository.repository_querys import RepositoryQuerys


class VisualizarVoos(BaseService):
    tabela = RepositoryQuerys
    dados = tabela("voos")
