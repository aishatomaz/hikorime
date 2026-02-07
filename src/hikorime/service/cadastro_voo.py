from hikorime.service.base_service import BaseService
from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.models.enums.status_voo import StatusVoo

class CadastroVooService(BaseService):
    """docstring for CadastroVooService."""

    def __init__(self, repo: RepositoryQuerys):
        self.repo = repo

    def save(
        self,
        data_saida,
        data_cheg,
        hora_saida,
        hora_chega,
        local_saida,
        destino,
        id_piloto,
        aviao,
        quant_vagas,
        status_voo: StatusVoo,
    ):
        return self.repo.save(
            data_saida=data_saida,
            data_cheg=data_cheg,
            hora_saida=hora_saida,
            hora_chega=hora_chega,
            local_saida=local_saida,
            destino=destino,
            id_piloto=id_piloto,
            aviao=aviao,
            quant_vagas=quant_vagas,
            status_voo=status_voo,
        )
