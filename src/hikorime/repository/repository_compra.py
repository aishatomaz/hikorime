from warnings import deprecated
from datetime import datetime, date

from hikorime.repository.repository_connection import RepositoryConnection
from hikorime.repository.repository_querys import RepositoryQuerys


class RepositoryCompra(RepositoryQuerys):
    """
    Classe do repositório para eventos específicos ou consultas mais detalhadas.
    Suas funções serão utilizadas pela camada de Service
    para validar regras de negócio.
    """

    def __init__(self, table_name: str):
        super().__init__(table_name)
        self.connection = RepositoryConnection()
        self.table_name = table_name

    def verificar_quantidade_compras_passageiro_maior_igual_3(
        self,
        passageiro_id: int,
    ) -> bool:
        """Verifica se existem passageiros com 3 ou mais compras registradas.

        Executa uma query no banco para contar quantas compras cada passageiro realizou
        e retorna True se houver algum passageiro com 3 ou mais compras.

        Returns:
            bool: True se houver passageiros com 3 ou mais compras, False caso contrário.
        """

        data = {"passageiro_id": passageiro_id}

        query = """
        SELECT id_passageiro, COUNT(*) as Total
        FROM compras
        WHERE id_passageiro = :passageiro_id
        GROUP BY id_passageiro
        HAVING COUNT(*) >= 3
        """
        result = self.connection.get_one(query, data)
        return bool(result)

    @deprecated(
        "Mudado para 'verificar_data_cupom_passageiro', para fazer a verificacao correta"
    )
    def verificar_data_validade_maior_que_hoje(
        self,
    ) -> bool:
        """Verifica se existem cupons com validade maior que a data atual.

        Executa uma query no banco para buscar cupons válidos.

        Returns:
            bool: True se houver cupons válidos, False caso contrário.
        """
        query = """SELECT validade FROM cupons WHERE validade >= date('now')"""
        result = self.connection.get_many(query)
        return bool(result)

    def get_compras(self, passageiro_id: int) -> list[dict]:
        """
        Retorna todas as compras realizadas por um passageiro, ordenadas pela data de compra.

        Args:
            passageiro_id (int): O ID do passageiro cujas compras serao recuperadas.

        Returns:
            list[dict]: Lista de dicionarios com as compras do passageiro.
        """

        data = {"passageiro_id": passageiro_id}
        query = """
            SELECT               
                id_compra,
                data_compra,
                valor_pago,
                valor_desconto,
                valor_total,
                tipo_pagamento
            FROM compras
            WHERE id_passageiro = :passageiro_id
            ORDER BY data_compra DESC
        """
        return RepositoryConnection().get_many(query, data)

    def get_valid_cupom_by_passageiro(self, passageiro_id: int):
        """Retorna cupons válidos para o passageiro que ainda não foram usados."""
        sql = """
            SELECT id_cupom, percentual_desconto, validade
            FROM cupons
            WHERE id_passageiro = :passageiro_id 
                AND validade >= date('now')
                AND usado = 0
                AND status = 'DISPONIVEL'
            LIMIT 1
        """
        data = {"passageiro_id": passageiro_id}
        return RepositoryConnection().get_one(sql, data)

    def get_cupons_by_passageiro(self, passageiro_id: int):
        """Retorna todos os cupons do passageiro com seus status."""
        sql = """
            SELECT id_cupom, percentual_desconto, validade, status, usado, data_criacao
            FROM cupons
            WHERE id_passageiro = :passageiro_id
            ORDER BY data_criacao DESC
        """
        data = {"passageiro_id": passageiro_id}
        return RepositoryConnection().get_many(sql, data)

    def get_passagens_by_passageiro(self, passageiro_id: int) -> list[dict]:
        """Retorna todas as passagens associadas ao passageiro com dados do voo."""

        data = {"passageiro_id": passageiro_id}
        sql = """
            SELECT 
                p.id_passagem,
                p.valor_pago,
                p.data_compra,
                v.id_voo,
                v.local_origem,
                v.local_destino,
                v.data_hora_partida,
                v.valor_base_passagem
            FROM passagens p
            JOIN voos v ON v.id_voo = p.id_voo
            WHERE p.id_passageiro = :passageiro_id
            ORDER BY p.data_compra DESC
        """
        return RepositoryConnection().get_many(sql, data)

    def get_valor_bagagens_by_passageiro_id(self, passageiro_id: int) -> list[dict]:
        """Retorna todas as bagagens associadas ao passageiro com seus valores."""

        data = {"passageiro_id": passageiro_id}
        sql = """
            SELECT id_bagagem, tipo_bagagem, peso, valor_bagagem
            FROM bagagens
            WHERE id_passageiro = :passageiro_id
            ORDER BY data_criacao DESC
        """
        return RepositoryConnection().get_many(sql, data)

    def marcar_cupom_como_usado(self, cupom_id: int):
        """Marca um cupom como usado após ser aplicado em uma compra."""
        query = """
            UPDATE cupons
            SET usado = 1, status = 'INDISPONIVEL'
            WHERE id_cupom = :cupom_id
        """
        data = {"cupom_id": cupom_id}
        return RepositoryConnection().update(query, data)

    def criar_cupom(
        self, passageiro_id: int, percentual_desconto: float, validade: date
    ) -> int:
        """Cria um novo cupom para um passageiro."""
        query = """
            INSERT INTO cupons (id_passageiro, percentual_desconto, validade, status, usado)
            VALUES (:passageiro_id, :percentual_desconto, :validade, 'DISPONIVEL', 0)
        """
        data = {
            "passageiro_id": passageiro_id,
            "percentual_desconto": percentual_desconto,
            "validade": validade,
        }
        return RepositoryConnection().save(query, data)

    def salvar_compra(self, compra_data: dict) -> int:
        """Salva uma nova compra no banco de dados."""
        query = """
            INSERT INTO compras (
                id_passageiro, id_passagem, id_bagagem, id_cupom,
                data_compra, tipo_pagamento, valor_pago, valor_desconto, valor_total
            )
            VALUES (
                :id_passageiro, :id_passagem, :id_bagagem, :id_cupom,
                :data_compra, :tipo_pagamento, :valor_pago, :valor_desconto, :valor_total
            )
        """
        return RepositoryConnection().save(query, compra_data)

    def get_tickets_disponiveis(
        self, local_origem: str, local_destino: str
    ) -> list[dict]:
        """Busca passagens disponíveis com filtros opcionais."""
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

    def calcular_valor_bagagem(self, peso: float) -> float:
        """Calcula o valor da bagagem baseado no peso."""
        VALOR_FIXO = 50.0
        TAXA_VARIAVEL = 5.0
        valor_bagagem = VALOR_FIXO + (peso * TAXA_VARIAVEL)
        return round(valor_bagagem, 2)

    def count_compras_passageiro(self, id_passageiro: int) -> int:
        """Conta o total de compras de um passageiro."""
        sql = (
            "SELECT COUNT(*) as total FROM compras WHERE id_passageiro = :id_passageiro"
        )
        data = {"id_usuario": id_passageiro}
        result = self.connection.get_one(sql, data)
        return result["total"] if result else 0

