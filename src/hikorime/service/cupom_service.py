from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService


class CupomService(BaseService):
    def __init__(self):
        self.repo = RepositoryQuerys("cupom")

    def save(
        self, percentual_desconto, validade
    ):  # TODO: verificar, status: StatusCupom
        return self.repo.save(
            percentual_desconto=percentual_desconto, validade=validade
        )

