from hikorime.repository.repository_connection import RepositoryConnection


class RepositoryPassagem:
    """Repositório para gerenciar passagens e tickets no banco de dados."""

    def __init__(self):
        self.conn = RepositoryConnection()

    def get_passagem_by_passageiro(self, passageiro_id: int):
        """Retorna todas as passagens de um passageiro, incluindo dados do voo relacionado.

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
                p.id_passagem,
                p.assento,
                p.valor_pago,
                p.data_compra,
                v.id_voo,
                v.local_origem,
                v.local_destino,
                v.data_hora_partida,
                v.data_hora_chegada,
                v.valor_base_passagem,
                v.terminal,
                v.portao_embarque
            FROM passagens p
            JOIN voos v ON v.id_voo = p.id_voo
            WHERE p.id_passageiro = :passageiro_id
            ORDER BY p.data_compra DESC
        """

        passagens = RepositoryConnection().get_many(sql, data)

        if not passagens:
            raise ValueError(
                f"Nenhuma passagem encontrada para o passageiro ID {passageiro_id}"
            )

        return passagens

    def get_tickets_disponiveis(self, local_origem: str = None, local_destino: str = None):
        """Busca voos disponíveis com assentos livres.

        Args:
            local_origem (str, optional): Cidade/local de origem.
            local_destino (str, optional): Cidade/local de destino.

        Returns:
            List[Dict]: Lista de voos disponíveis com informações de assentos.
        """
        query = """
            SELECT 
                v.id_voo,
                v.local_origem,
                v.local_destino,
                v.data_hora_partida,
                v.data_hora_chegada,
                v.valor_base_passagem,
                v.terminal,
                v.portao_embarque,
                a.modelo as modelo_aeronave,
                COUNT(p.id_passagem) as assentos_vendidos,
                a.total_assentos,
                (a.total_assentos - COUNT(p.id_passagem)) as assentos_disponiveis
            FROM voos v
            JOIN aeronaves a ON a.id_aeronave = v.id_aeronave
            LEFT JOIN passagens p ON p.id_voo = v.id_voo
            WHERE 1=1
        """
        
        data = {}
        
        if local_origem:
            query += " AND v.local_origem = :local_origem"
            data["local_origem"] = local_origem
        
        if local_destino:
            query += " AND v.local_destino = :local_destino"
            data["local_destino"] = local_destino
        
        query += """
            GROUP BY v.id_voo
            HAVING assentos_disponiveis > 0
            ORDER BY v.data_hora_partida ASC
        """
        
        return RepositoryConnection().get_many(query, data)

    def get_voo_by_id(self, voo_id: int):
        """Obtém informações de um voo específico.

        Args:
            voo_id (int): ID do voo.

        Returns:
            Dict: Informações do voo.
        """
        data = {"voo_id": voo_id}

        sql = """
            SELECT
                v.id_voo,
                v.local_origem,
                v.local_destino,
                v.data_hora_partida,
                v.data_hora_chegada,
                v.valor_base_passagem,
                v.terminal,
                v.portao_embarque,
                a.modelo as modelo_aeronave,
                a.total_assentos
            FROM voos v
            JOIN aeronaves a ON a.id_aeronave = v.id_aeronave
            WHERE v.id_voo = :voo_id
        """

        return RepositoryConnection().get_one(sql, data)

    def verificar_assentos_disponiveis(self, voo_id: int) -> int:
        """Verifica quantos assentos estão disponíveis em um voo.

        Args:
            voo_id (int): ID do voo.

        Returns:
            int: Número de assentos disponíveis.
        """
        data = {"voo_id": voo_id}

        sql = """
            SELECT 
                (a.total_assentos - COUNT(p.id_passagem)) as assentos_disponiveis
            FROM voos v
            JOIN aeronaves a ON a.id_aeronave = v.id_aeronave
            LEFT JOIN passagens p ON p.id_voo = v.id_voo
            WHERE v.id_voo = :voo_id
            GROUP BY v.id_voo
        """

        result = RepositoryConnection().get_one(sql, data)
        return result.get("assentos_disponiveis", 0) if result else 0

    def get_assentos_ocupados(self, voo_id: int):
        """Obtém a lista de assentos ocupados em um voo.

        Args:
            voo_id (int): ID do voo.

        Returns:
            List[Dict]: Lista de assentos ocupados.
        """
        data = {"voo_id": voo_id}

        sql = """
            SELECT 
                p.id_passagem,
                p.assento,
                p.id_passageiro
            FROM passagens p
            WHERE p.id_voo = :voo_id
            ORDER BY p.assento ASC
        """

        return RepositoryConnection().get_many(sql, data)
