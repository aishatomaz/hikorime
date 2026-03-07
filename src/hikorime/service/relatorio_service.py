from hikorime.repository.repository_relatorio import RelatorioRepository
import json 
class RelatorioService:
    '''O service de Relatório foi alterado para gerear os relatórios em JSON. Importa as consultas específicas de Repository e
    retorna um JSON dessas consultas'''
    def __init__(self):
        self.repo = RelatorioRepository()

    def quantidade_voos_semanal(self):
        dados = self.repo.get_quantidade_voo_semanal()
        resultado_json = json.dumps(dados, indent=4, ensure_ascii=False)
        return resultado_json

    def quantidade_voo_mensal(self):
        dados = self.repo.get_quantidade_voo_mensal()
        resultado_json = json.dumps(dados, indent=4, ensure_ascii=False)
        return resultado_json
    
    def quantidade_voo_anual(self):
        dados = self.repo.get_quantidade_voo_anual()
        resultado_json = json.dumps(dados, indent=4, ensure_ascii=False)
        return resultado_json
    
    def faturamento_semanal(self):
        dados = self.repo.get_faturamento_semanal()
        resultado_json = json.dumps(dados, indent=4, ensure_ascii=False)
        return resultado_json

    def faturamento_mensal(self):
        dados = self.repo.get_faturamento_mensal()
        resultado_json = json.dumps(dados, indent=4, ensure_ascii=False)
        return resultado_json
    
    def faturamento_anual(self):
        dados = self.repo.get_faturamento_anual()
        resultado_json = json.dumps(dados, indent=4, ensure_ascii=False)
        return resultado_json
    
    def passageiro_comprou_mais_passagens(self):
        dados = self.repo.get_passageiro_comprou_mais_passagens()
        resultado_json = json.dumps(dados, indent=4, ensure_ascii=False)
        return resultado_json

    def todos_relatorios(self, arquivo="relatorios.json"):
        relatorios = {
            "quantidade_voos_semanal": self.repo.get_quantidade_voo_semanal(),
            "quantidade_voos_mensal": self.repo.get_quantidade_voo_mensal(),
            "quantidade_voos_anual": self.repo.get_quantidade_voo_anual(),
            "faturamento_semanal": self.repo.get_faturamento_semanal(),
            "faturamento_mensal": self.repo.get_faturamento_mensal(),
            "faturamento_anual": self.repo.get_faturamento_anual(),
            "top_passageiros": self.repo.get_passageiro_comprou_mais_passagens()
        }

        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(relatorios, f, indent=4, ensure_ascii=False)
        return relatorios