import pandas as pd
import matplotlib.pyplot as plt
from hikorime.repository.repository_analytics import AnalyticsRepository

class AnalyticsService:
    def __init__(self):
        self.repo = AnalyticsRepository()
    '''A classe possui o objetivo de acessar o Banco de dados diretamente, buscando consultas específicas para gerara gráficos no relatório.
    Aqui, ela não usa as bibibliotas (no caso, pandas e matplotlib), apenas realiza as consultas que serão utilizadas em Service, posteriormente.'''

    def quantidade_voo_semanal(self):
        dados = self.repo.get_quantidade_voo_semanal()
        df = pd.DataFrame(dados, columns=["semana", "quantidade"])
        df.plot(
            kind="bar",
            x="semana",
            y="quantidade",
            legend=False,
        )
        plt.title("Quantidade de voos na semana atual")
        plt.show()
        return df

    def quantidade_voo_mensal(self):
        dados = self.repo.get_quantidade_voo_mensal()
        df = pd.DataFrame(dados, columns=["mes", "quantidade"])
        df.plot (
            kind="bar",
            x="mes",
            y="quantidade",
            legend=False,
        )
        plt.title("Quantidade de voos no mês atual")
        plt.show()
        return df

    def quantidade_voo_anual(self):
        dados = self.repo.get_quantidade_voo_mensal()
        df = pd.DataFrame(dados, columns=["ano", "quantidade"])
        df.plot (
            kind="bar",
            x="ano",
            y="quantidade",
            legend=False,
        )
        plt.title("Quantidade de voos no ano atual")
        plt.show()
        return df

    def faturamento_semanal(self):
        dados = self.repo.get_faturamento_mensal()
        df = pd.DataFrame(dados, columns=["mes", "faturamento"])
        df["mes"] = pd.to_datetime(df["mes"])
        df = df.sort_values("mes")
        df.plot(
            kind="bar",
            x="mes",
            y="faturamento",
            legend=False,
        )
        plt.xlabel("Mês")
        plt.ylabel("Faturamento")
        plt.title("Faturamento Semanal")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        return df

    def faturamento_mensal(self):
        dados = self.repo.get_faturamento_mensal()
        df = pd.DataFrame(dados, columns=["mes", "faturamento"])
        df["mes"] = pd.to_datetime(df["mes"])
        df = df.sort_values("mes")
        df.plot(
            kind="bar",
            x="mes",
            y="faturamento",
            legend=False,
        )
        plt.xlabel("Mês")
        plt.ylabel("Faturamento")
        plt.title("Faturamento Mensal")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        return df

    def faturamento_anual(self):
        dados = self.repo.get_faturamento_anual()
        df = pd.DataFrame(dados, columns=["ano", "faturamento"])
        df["ano"] = pd.to_datetime(df["ano"])
        df = df.sort_values("ano")
        df.plot(
            kind="bar",
            x="ano",
            y="faturamento",
            legend=False,
        )
        plt.xlabel("Ano")
        plt.ylabel("Faturamento")
        plt.title("Faturamento Anual")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        return df

    def grafico_passageiro_comprou_mais_passagens(self):
        dados = self.repo.get_passageiro_comprou_mais_passagens()
        df = pd.DataFrame(dados, columns=["passageiro_id", "quantidade"])
        df["passageiro_id"] = df["passageiro_id"].astype(str)
        df.plot(
            kind="bar",
            x="passageiro_id",
            y="quantidade",
            legend=False,
        )
        plt.xlabel("Passageiro ID")
        plt.ylabel("Quantidade de Passagens")
        plt.title("Top 5 passageiros que mais compraram passagens")
        plt.tight_layout()
        plt.show()
        return df