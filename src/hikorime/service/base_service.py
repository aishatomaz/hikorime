from typing import Dict, Optional
from warnings import deprecated
from hikorime.repository.repository_querys import RepositoryQuerys


class BaseService:
    """
    Classe base para outras classes do tipo servico
    Lembre de fazer a funcao save para cada service individualmente
    """

    def __init__(self, repository: RepositoryQuerys):
        self.repo = repository

    def save(
        self, model
    ):  # Gracas ao modulo basemodels, posso finalmente fazer um save generico
        """
        Método genérico para salvar um modelo Pydantic no banco de dados.

        Args:
            model: Instância do modelo Pydantic a ser salva.

        Returns:
            dict: Dados salvos (id, nome_voo, etc.)
        """
        model_dict = model.model_dump()  # Converte o modelo Pydantic para um dicionario
        return self.repo.save(
            **model_dict
        )  # Passa os dados como kwargs para o repositorio

    @deprecated("Jamais use em producao, debug e teste apenas")
    def get_all(self): # TODO: ???
        """
        Retorna todas as linhas e colunas de uma tabela.

        returns:
            Tudo da tabela
        """
        return self.repo.get_all()

    def get_by_id(self, id: int) -> int | None:
        """
        Retira um id especifico da tabela:

        Args:
            id: O id que queira buscar na tabela

        returns:
            int | None: um int se encontrado, caso não, None
        """
        if self.repo.get_by_id(id) is not None:
            return id
        else:
            raise ValueError(f"id '{id}' não existe")

    def get_by_column_name(self, column_name: str, value: str) -> Optional[Dict]:
        """
        Retira o(s) valor(es) exato(s) de uma coluna especifica
        Args:
            column_name: O nome da coluna da tabela a ser buscado
            value: o valor exato que quer buscar

        Returns:
            Dict | ValueError: Um dicionario com o(s) valores encontrados
        """
        if value.rstrip() is None or "":
            raise ValueError("ERROR: Falta o valor para iniciar a busca")
        elif column_name.rstrip() is None or "":
            raise ValueError("ERROR: Falta o Nome da coluna, para iniciar a busca")
        else:
            return self.repo.get_by_column_name(column_name, value)

    def get_like_by_column_name(self, column_name: str, value: str | int):
        """
        Retorna o(s) valor(es) parciais(s) de uma coluna especifica

        Args:
            column_name: O nome da coluna da tabela a ser buscado
            value: o valor parcial que quer buscar (se precisar de um valor exato, use get_by_column_name)

        Returns
            Dict | ValueError: Um dicionario com o(s) valores encontrados.
        """
        return self.repo.get_like_by_column_name(column_name, value)

    def delete_by_id(self, id: int):
        """
        Deleta uma linha  usando seu id

        Args:
            id: O id do item a ser deletado.

        Returns:
            dict | None: Retorna um dicionario do item alterado ou None caso nao encontrado
        """
        id_exists = self.get_by_id(id)  # Verifica se o id existe

        if id_exists:
            return self.repo.delete_by_id(id)
        else:
            return None

    def get_quantity_of_rown(self) -> Dict[str, int] | None:
        """
        retorna a quantidade de linhas de uma coluna

        Returns:
            Dict | None: Um dicionario contendo a quantidade de linhas da tabela, Caso a tabela nao exista, None
        """
        return self.repo.get_quantity_of_rown()

    def update_column(self, id: int, data: dict):
        """
        Um put, vai apenas mudar uma coluna da linha da tabela
        exemplo, posso mudar 'invers' para 'sudo invers', sem alterar qualquer outro dado dele.
        Args:
            id: o id da linha que queira mudar
            data: o dict que vai fazer as mudancas, recomendo ver o exemplo de funcionamento abaixo
        """
        return self.repo.update_column(id, data)

    def table_name(self) -> str:
        """Retorna o nome da tabela atual"""
        return self.repo.table_name
