from fastapi import HTTPException
from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
from hikorime.repository.repository_passagem import RepositoryPassagem
from hikorime.models.basemodels.bm_passagem import Passagem


class PassagemService(BaseService):
    def __init__(self):
        self.repo = RepositoryQuerys("passagens")
        self.service = RepositoryPassagem()

    def create_passagem(self, passagem_data):
        """
        Cria uma nova passagem

        Args:
            passagem_data: Dicionario com os dados da passagem a ser salva.

        Returns:
            dict: Dados da passagem salva
        """
        try:
            passagem = Passagem(**passagem_data)
            return self.save(passagem)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao comprar a passagem: {str(e)}")

    def get_passagem_by_passageiro(self, passageiro_id: int):
        """
        Retorna todas as passagens de um passageiro, incluindo dados do voo relacionado.

        Args:
            passageiro_id: O ID do passageiro cujas passagens queremos recuperar.

        Returns:
            List[Dict]: Lista de dicionários representando as passagens, incluindo detalhes do voo.

        Raises:
            ValueError: Caso o passageiro não tenha passagens registradas.
        """
        self.service.get_passagem_by_passageiro(passageiro_id)
