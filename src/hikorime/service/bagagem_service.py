from datetime import datetime
from typing import Dict
from hikorime.service.base_service import BaseService
from hikorime.repository.repository_bagagem import RepositoryBagagem


class BagagemService(BaseService):
    def __init__(self):
        self.service = RepositoryBagagem("bagagens")

    def get_quantidade_bagagem_by_passageiro_id(self, id: int) -> Dict | None:
        self.service.get_quantidade_bagagem_by_passageiro(id)

    def get_bagagem_by_data(self, passageiro_id: int, data: datetime) -> Dict | None:
        self.service.get_bagagem_by_data(passageiro_id, data)
