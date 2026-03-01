from hikorime.repository.repository_connection import RepositoryConnection


class AnalyticsRepository:
    def __init__(self):
        self.conn = RepositoryConnection()

    def get_quantidade_voo_semanal(self):
        ''''''
        query = """
        SELECT COUNT(*)
        FROM voos
        WHERE strftime('%Y-%W', data_hora_partida) = strftime('%Y-%W', 'now');
        """
        return self.conn.get_many(query)


    def get_quantidade_voo_mensal(self):
        query ="""
        SELECT COUNT(*)
        FROM voos
        WHERE strftime('%Y-%W', data_hora_partida) = strftime('%Y-%M', 'now');
        """
        return self.conn.get_many(query)


    def get_quantidade_voo_anual(self):
        query ="""
        SELECT COUNT(*)
        FROM voos
        WHERE strftime('%Y', data_hora_partida) = strftime('%Y', 'now');
        """
        return self.conn.get_many(query)


    def get_faturamento_semanal(self):
        query = """
        SELECT COALESCE(SUM(valor_total), 0) AS faturamento_semana
        FROM compras
        WHERE data_compra >= date('now', 'weekday 1', '-7 days')
        AND data_compra < date('now', 'weekday 1');
        """
        return self.conn.get_many(query)


    def get_faturamento_mensal(self):
        query = """SELECT COALESCE(SUM(valor_total), 0) AS faturamento_mes
        FROM compras
        WHERE data_compra >= date('now', 'start of month')
        AND data_compra < date('now', 'start of month', '+1 month');
        """
        return self.conn.get_many(query)


    def get_faturamento_anual(self):
        query = """SELECT COALESCE(SUM(valor_total), 0) AS faturamento_ano
        FROM compras
        WHERE data_compra >= date('now', 'start of year')
        """
        return self.conn.get_many(query)


    def get_passageiro_comprou_mais_passagens(self):
        query = """
        SELECT passageiro_id, COUNT(*) as quantidade
        FROM passagens_vendidas 
        GROUP BY passageiro_id
        ORDER BY quantidade DESC
        LIMIT 5;
        """
        return self.conn.get_many(query)
        
        
