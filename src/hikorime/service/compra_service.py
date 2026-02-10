from hikorime.service.base_service import BaseService
from hikorime.repository.repository_querys import RepositoryQuerys


class CompraService(BaseService):
    def __init__(self):
        self.repo = RepositoryQuerys("compra")

    def save(self, data_compra, valor_total, pagamento):
        return self.repo.save(
            data_compra=data_compra, valor_total=valor_total, pagamento=pagamento
        )

