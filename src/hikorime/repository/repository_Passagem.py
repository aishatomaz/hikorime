from hikorime.repository.repository_connection import RepositoryConnection


class RepositoryPassagem():
    def get_by_passageiro(self, passageiro_id: int):

        data = {"passageiro_id": passageiro_id}

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
