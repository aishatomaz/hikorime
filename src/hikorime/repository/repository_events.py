from hikorime.repository.repository_connection import RepositoryConnection

'''Classe do repositório para eventos específicos ou consultas mais detalhadas. Suas funções serão utilizadas pela camada de Service
    para validar regras de negócio.'''

class RepositoryEvents:
    def __init__(self):
        self.connection = RepositoryConnection()

    def verificar_quantidade_compras_passageiro_maior_igual_3(self) -> bool:
       """Verifica se existem passageiros com 3 ou mais compras registradas.

        Executa uma query no banco para contar quantas compras cada passageiro realizou
        e retorna True se houver algum passageiro com 3 ou mais compras.

        Returns:
            bool: True se houver passageiros com 3 ou mais compras, False caso contrário.
        """
       query = """SELECT passageiro_id, COUNT(*) as Total FROM passagens_vendidas GROUP BY passageiro_id HAVING COUNT(*) >= 3"""   
       result = self.connection.query(query)
       return bool(result)
    
    def verificar_data_validade_maior_que_hoje(self) -> bool:
        """Verifica se existem cupons com validade maior que a data atual.

        Executa uma query no banco para buscar cupons válidos.

        Returns:
            bool: True se houver cupons válidos, False caso contrário.
        """
        query = """SELECT validade FROM cupom WHERE validade >= date('now')"""
        result = self.connection.query(query)
        return bool(result)

    
