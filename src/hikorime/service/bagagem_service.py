from datetime import datetime
from typing import Dict, List
from fastapi import HTTPException

from hikorime.repository.repository_querys import RepositoryQuerys
from hikorime.service.base_service import BaseService
from hikorime.repository.repository_bagagem import RepositoryBagagem


class BagagemService(BaseService):
    """Serviço para gerenciar bagagens dos passageiros."""

    VALOR_FIXO = 50.0
    TAXA_VARIAVEL = 5.0
    PESO_MAXIMO = 10.0

    def __init__(self):
        self.service = RepositoryBagagem("bagagens")

    def get_quantidade_bagagem_by_passageiro_id(self, id: int) -> Dict | None:
        """Obtém a quantidade de bagagens de um passageiro."""
        return self.service.get_quantidade_bagagem_by_passageiro(id)

    def get_bagagem_by_data(self, passageiro_id: int, data: datetime) -> Dict | None:
        """Obtém bagagens de um passageiro por data."""
        return self.service.get_bagagem_by_date(passageiro_id, data)

    def calcular_valor_bagagem(self, peso: float) -> float:
        """Calcula o valor da bagagem baseado no peso.
        
        Fórmula: VALOR_FIXO + (peso * TAXA_VARIAVEL)
        - VALOR_FIXO: R$ 50,00
        - TAXA_VARIAVEL: R$ 5,00 por kg
        - PESO_MAXIMO: 10 kg

        Args:
            peso (float): Peso da bagagem em kg.

        Returns:
            float: Valor calculado da bagagem.

        Raises:
            HTTPException: Se o peso for inválido ou exceder o limite.
        """
        try:
            peso = float(peso)
            
            if peso <= 0:
                raise ValueError("O peso deve ser maior que zero")
            
            if peso > self.PESO_MAXIMO:
                raise ValueError(f"O peso máximo permitido é {self.PESO_MAXIMO} kg")
            
            valor = self.VALOR_FIXO + (peso * self.TAXA_VARIAVEL)
            return round(valor, 2)
        
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def criar_bagagem(self, passageiro_id: int, tipo_bagagem: str, peso: float) -> dict:
        """Cria uma bagagem para um passageiro.

        Args:
            passageiro_id (int): ID do passageiro.
            tipo_bagagem (str): Tipo da bagagem ('normal' ou 'frágil').
            peso (float): Peso da bagagem em kg.

        Returns:
            dict: Informações da bagagem criada.

        Raises:
            HTTPException: Se houver erro na criação.
        """
        try:
            # Validar tipo de bagagem
            tipos_validos = ['normal', 'frágil', 'fragil']
            if tipo_bagagem.lower() not in tipos_validos:
                raise ValueError(f"Tipo de bagagem inválido. Tipos válidos: {tipos_validos}")
            
            # Calcular valor
            valor_bagagem = self.calcular_valor_bagagem(peso)
            
            # Preparar dados
            bagagem_data = {
                "id_passageiro": passageiro_id,
                "tipo_bagagem": tipo_bagagem,
                "peso": peso,
                "valor_bagagem": valor_bagagem
            }
            
            # Salvar bagagem
            bagagem_id = self.service.save(**bagagem_data)
            
            return {
                "id_bagagem": bagagem_id,
                "id_passageiro": passageiro_id,
                "tipo_bagagem": tipo_bagagem,
                "peso": peso,
                "valor_bagagem": valor_bagagem
            }
        
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Erro ao criar bagagem: {str(e)}"
            )

    def get_bagagens_by_passageiro(self, passageiro_id: int) -> List[Dict]:
        """Obtém todas as bagagens de um passageiro.

        Args:
            passageiro_id (int): ID do passageiro.

        Returns:
            List[Dict]: Lista de bagagens do passageiro.
        """
        return self.service.get_bagagens_by_passageiro(passageiro_id)

    def calcular_valor_total_bagagens(self, passageiro_id: int) -> float:
        """Calcula o valor total das bagagens de um passageiro.

        Args:
            passageiro_id (int): ID do passageiro.

        Returns:
            float: Valor total das bagagens.
        """
        bagagens = self.get_bagagens_by_passageiro(passageiro_id)
        
        if not bagagens:
            return 0.0
        
        total = sum(float(b.get("valor_bagagem", 0)) for b in bagagens)
        return round(total, 2)
