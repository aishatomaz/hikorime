from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
from hikorime.models.statuscupom import StatusCupom

class CupomService(BaseService):
    def __init__(self, repo: RepositoryQuerys):
        self.repo = repo

    def save(self, percentual_desconto, validade, status: StatusCupom):
        return self.repo.save(
            percentual_desconto = percentual_desconto,
            validade = validade)
    