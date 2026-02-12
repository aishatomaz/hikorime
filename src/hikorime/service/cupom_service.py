from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
from hikorime.repository.repository_events import RepositoryEvents

'''Salva os relacionados à cupom no Banco de Dados.'''
class CupomService(BaseService):
    events_repository: RepositoryEvents

    def __init__(self):
        self.repo = RepositoryQuerys("cupom")
        self.events_repository = RepositoryEvents()

    def save(
        self, percentual_desconto, validade 
    ):
        return self.repo.save(
            percentual_desconto=percentual_desconto, validade=validade 
        )

# Regras de negócio 

    def verifificar_passageiro_apto_aplicar_cupom(self) -> bool:
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