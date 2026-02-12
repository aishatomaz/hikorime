from hikorime.service.base_service import BaseService
from hikorime.repository.repository_querys import RepositoryQuerys

'''Classe salva os valores de Compra no Banco de Dados.'''
class CompraService(BaseService):
    def __init__(self):
        self.repo = RepositoryQuerys("compra")

    def save(self, data_compra, valor_total, pagamento):
        return self.repo.save(
            data_compra=data_compra, valor_total=valor_total, pagamento=pagamento
        )

# Regras de negócio

    def calcular_total(self, passageiro_id: int):
        '''Calcula o valor total da compra de um passageiro.

        A função soma o valor da última passagem adquirida pelo passageiro
        com o valor das bagagens (quando disponível) e aplica o desconto de cupom,
        caso o passageiro seja elegível.

        Args:
            passageiro_id (int): ID do passageiro para o qual o total será calculado.

        Returns:
            float: Valor total da compra após somar passagens, bagagens e aplicar desconto do cupom.
                Retorna 0 se o passageiro não possuir passagens registradas.
        '''
        return 