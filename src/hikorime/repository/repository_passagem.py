from hikorime.repository.repository_connection import RepositoryConnection


class RepositoryPassagem:
    def get_passagem_by_passageiro(self, passageiro_id: int):
        """
        Retorna todas as passagens de um passageiro, incluindo dados do voo relacionado.

        Args:
            passageiro_id: O ID do passageiro cujas passagens queremos recuperar.

        Returns:
            List[Dict]: Lista de dicionários representando as passagens, incluindo detalhes do voo.

        Raises:
            ValueError: Caso o passageiro não tenha passagens registradas.
        """
        data = {"passageiro_id": passageiro_id}

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

        passagens = RepositoryConnection().get_many(sql, data)

        if not passagens:
            raise ValueError(
                f"Nenhuma passagem encontrada para o passageiro ID {passageiro_id}"
            )

        return passagens
