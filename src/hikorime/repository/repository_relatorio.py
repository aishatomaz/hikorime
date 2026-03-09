from hikorime.repository.repository_connection import RepositoryConnection


class RelatorioRepository:
    """A classe possui o objetivo de acessar o Banco de dados diretamente, buscando consultas específicas para gerara gráficos no relatório.
    Aqui, ela não usa as bibibliotas (no caso, pandas e matplotlib), apenas realiza as consultas que serão utilizadas em Service, posteriormente."""

    def __init__(self):
        self.conn = RepositoryConnection()

    def get_quantidade_voo_semanal(self):
        query = """
        SELECT 
        strftime('%Y', data_saida) || '-S' || strftime('%W', data_saida) AS semana,
        COUNT(*) AS quantidade_voos
        FROM voos
        GROUP BY semana
        ORDER BY semana;
        """
        return self.conn.get_many(query)

    def get_quantidade_voo_mensal(self):
        query = """
        SELECT 
        strftime('%Y-%m', data_saida) AS mes,
        COUNT(*) AS quantidade_voos
        FROM voos
        GROUP BY mes
        ORDER BY mes;
        """
        return self.conn.get_many(query)

    def get_quantidade_voo_anual(self):
        query = """
        SELECT 
        strftime('%Y', data_saida) AS ano,
        COUNT(*) AS quantidade_voos
        FROM voos
        GROUP BY ano
        ORDER BY ano;
        """
        return self.conn.get_many(query)

    def get_faturamento_semanal(self):
        query = """
        SELECT 
        strftime('%Y', data_compra) || '-S' || strftime('%W', data_compra) AS semana,
        SUM(valor_compra) AS faturamento
        FROM compras
        GROUP BY semana
        ORDER BY semana;
        """
        return self.conn.get_many(query)

    def get_faturamento_mensal(self):
        query = """
        SELECT 
        strftime('%Y-%m', data_compra) AS mes,
        SUM(valor_compra) AS faturamento
        FROM compras
        GROUP BY mes
        ORDER BY mes;
        """
        return self.conn.get_many(query)

    def get_faturamento_anual(self):
        query = """
        SELECT 
        strftime('%Y', data_compra) AS ano,
        SUM(valor_compra) AS faturamento
        FROM compras
        GROUP BY ano
        ORDER BY ano;
        """
        return self.conn.get_many(query)

    def get_passageiro_comprou_mais_passagens(self):
        query = """
        SELECT id_passageiro, COUNT(*) AS quantidade
        FROM passagens
        GROUP BY id_passageiro
        ORDER BY quantidade DESC
        LIMIT 5;
        """
        return self.conn.get_many(query)
