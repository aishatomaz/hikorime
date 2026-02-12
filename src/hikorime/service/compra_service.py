from hikorime.service.base_service import BaseService
from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.repository.repository_compra import RepositoryCompra

'''Classe salva os valores de Compra no Banco de Dados.'''
class CompraService(BaseService):
    events_repository: RepositoryCompra
    def __init__(self):
        self.repo = RepositoryQuerys("compra")
        self.events = RepositoryCompra()

    def save(self, data_compra, valor_total, pagamento):
        return self.repo.save(
            data_compra=data_compra, valor_total=valor_total, pagamento=pagamento
        )

# Regras de negócio

    def verificar_passageiro_apto_aplicar_cupom(self) -> bool:
        '''Verifica se o passageiro está apto a aplicar um cupom de desconto.

        A função checa duas condições:
        1. O passageiro possui 3 ou mais compras registradas.
        2. Existem cupons válidos disponíveis (com validade maior que a data atual).

        Ambas as condições devem ser verdadeiras para que o passageiro seja considerado apto.

        Returns:
            bool: True se o passageiro puder aplicar o cupom, False caso contrário.
        '''
        return (
            self.events_repository.verificar_quantidade_compras_passageiro_maior_igual_3()
            and
            self.events_repository.verificar_data_validade_maior_que_hoje()
        )

    def calcular_total(self, passageiro_id: int):
        '''Calcula o valor total da compra de um passageiro.
        TODO:
            *A função soma o valor da última passagem adquirida pelo passageiro
            com o valor das bagagens (quando disponível) e aplica o desconto de cupom,
            caso o passageiro seja elegível. 

            *Args:
                passageiro_id (int): ID do passageiro para o qual o total será calculado.

            *Returns:
                float: Valor total da compra após somar passagens, bagagens e aplicar desconto do cupom.
                    Retorna 0 se o passageiro não possuir passagens registradas.
        '''
        if self.verificar_passageiro_apto_aplicar_cupom():
            return
    
    def visualizar_compras(passageiro_id: int):
        return RepositoryCompra.vizualizar_compras(passageiro_id)