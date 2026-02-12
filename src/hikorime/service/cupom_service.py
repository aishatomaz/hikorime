from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
from hikorime.repository.repository_compra import RepositoryCompra

'''Salva os relacionados à cupom no Banco de Dados.'''
class CupomService(BaseService):
    events_repository: RepositoryCompra

    def __init__(self):
        self.repo = RepositoryQuerys("cupom")
        self.events_repository = RepositoryCompra()

    def save(
        self, percentual_desconto, validade 
    ):
        return self.repo.save(
            percentual_desconto=percentual_desconto, validade=validade 
        )

    