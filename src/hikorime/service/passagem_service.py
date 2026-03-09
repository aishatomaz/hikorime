from fastapi import HTTPException
from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
from hikorime.repository.repository_passagem import RepositoryPassagem
from hikorime.models.basemodels.bm_passagem import Passagem


class PassagemService(BaseService):
    """Serviço para gerenciar passagens e tickets de voos."""

    def __init__(self):
        self.repo = RepositoryQuerys("passagens")
        self.service = RepositoryPassagem()

    def create_passagem(self, passagem: Passagem) -> int:
        """Cria uma nova passagem.

        Args:
            passagem: dados da passagem a ser salva.

        Returns:
            int: ID da passagem salva

        Raises:
            HTTPException: Se houver erro na criação.
        """
        try:
            return self.save(passagem)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao comprar a passagem: {str(e)}")

    def get_passagem_by_passageiro(self, passageiro_id: int):
        """Retorna todas as passagens de um passageiro, incluindo dados do voo relacionado.

        Args:
            passageiro_id: O ID do passageiro cujas passagens queremos recuperar.

        Returns:
            List[Dict]: Lista de dicionários representando as passagens, incluindo detalhes do voo.

        Raises:
            ValueError: Caso o passageiro não tenha passagens registradas.
        """
        return self.service.get_passagem_by_passageiro(passageiro_id)

    def get_tickets_disponiveis(self, local_origem: str = None, local_destino: str = None):
        """Busca tickets (passagens) disponíveis com filtros opcionais.

        Args:
            local_origem (str, optional): Cidade/local de origem.
            local_destino (str, optional): Cidade/local de destino.

        Returns:
            List[Dict]: Lista de voos disponíveis com informações de assentos.

        Raises:
            HTTPException: Se houver erro na busca.
        """
        try:
            return self.service.get_tickets_disponiveis(local_origem, local_destino)
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Erro ao buscar tickets: {str(e)}"
            )

    def get_voo_by_id(self, voo_id: int):
        """Obtém informações de um voo específico.

        Args:
            voo_id (int): ID do voo.

        Returns:
            Dict: Informações do voo.
        """
        return self.service.get_voo_by_id(voo_id)

    def verificar_assentos_disponiveis(self, voo_id: int) -> int:
        """Verifica quantos assentos estão disponíveis em um voo.

        Args:
            voo_id (int): ID do voo.

        Returns:
            int: Número de assentos disponíveis.
        """
        return self.service.verificar_assentos_disponiveis(voo_id)

    def comprar_passagem(self, voo_id: int, passageiro_id: int, assento: str) -> int:
        """Realiza a compra de uma passagem.

        Args:
            voo_id (int): ID do voo.
            passageiro_id (int): ID do passageiro.
            assento (str): Número do assento.

        Returns:
            int: ID da passagem comprada.

        Raises:
            HTTPException: Se houver erro na compra.
        """
        try:
            passagem_data = Passagem(
                id_voo=voo_id,
                id_passageiro=passageiro_id,
                assento=assento
            )
            return self.create_passagem(passagem_data)
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Erro ao comprar passagem: {str(e)}"
            )