from hikorime.repository.repository_connection import RepositoryConnection

class RepositoryCompra:
    '''Classe do repositório para eventos específicos ou consultas mais detalhadas. Suas funções serão utilizadas pela camada de Service
    para validar regras de negócio.'''
    def __init__(self):
        self.connection = RepositoryConnection()

    def verificar_quantidade_compras_passageiro_maior_igual_3(self, passageiro_id: int, passagens_vendidas) -> bool:
        """Verifica se existem passageiros com 3 ou mais compras registradas.

        Executa uma query no banco para contar quantas compras cada passageiro realizou
        e retorna True se houver algum passageiro com 3 ou mais compras.

        Returns:
            bool: True se houver passageiros com 3 ou mais compras, False caso contrário.
        """

        data = {"passageiro_id": passageiro_id, "passagens_vendidas": passagens_vendidas}
        query = f"""SELECT :passageiro_id, COUNT(*) as Total FROM :passagens_vendidas GROUP BY :passageiro_id HAVING COUNT(*) >= 3"""   
        result = self.connection.query(query, data)
        return bool(result)
    
    def verificar_data_validade_maior_que_hoje(self, passageiro_id: int) -> bool:
        data = {"passageiro_id": passageiro_id}
        """Verifica se existem cupons com validade maior que a data atual.

        Executa uma query no banco para buscar cupons válidos.

        Returns:
            bool: True se houver cupons válidos, False caso contrário.
        """
        query = """SELECT validade FROM cupom WHERE validade >= date('now')"""
        result = self.connection.query(query, data)
        return bool(result)

    def vizualizar_compras(self, passageiro_id: int):
        data = {"passageiro_id": passageiro_id}
        query = """
            SELECT               
                data_compra,
                valor_pago,
                tipo_pagamento
            FROM compra
            WHERE passageiro_id = :passageiro_id
            ORDER BY data_compra DESC
        """
        return RepositoryConnection().query(query, data)