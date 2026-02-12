from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
from hikorime.repository.repository_Passagem import RepositoryPassagem

class PassagemService(BaseService):
    def __init__(self):
        self.repo = RepositoryQuerys("passagens_vendidas")

    def get_by_passageiro(self, passageiro_id: int):

        data = {"passageiro_id": passageiro_id}

        # TODO: Mudar para um classe repo

        # Faz um join entre passageiros e voos
        sql = """
            SELECT
                p.id,
                p.assento,
                p.valor_pago,
                p.data_compra,
                v.local_saida,
                v.destino,
                v.data_saida,
                v.hora_saida
            FROM passagens p
            JOIN voos v ON v.id = p.voo_id
            WHERE p.passageiro_id = :passageiro_id
            ORDER BY p.data_compra DESC
        """

        return RepositoryConnection().query(sql, data)