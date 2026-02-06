from abc import ABC

from hikorime.repository.repository_querys import RepositoryQuerys


class BaseService(ABC):
    """
    Classe base para outras classes do tipo servico
    Lembre de fazer a funcao save para cada service individualmente
    """

<<<<<<< HEAD
    def __init__(self, repository: RepositoryQuerys):
        self.repo = repository
=======
    def __init__(self, repository: RepositoryQuerys, table_name:str):
        self.repo = repository
        self.table_name = table_name

>>>>>>> 8779ceeed62d9e8522b5cf4d3f278eec7879cab8

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id: int):
        return self.repo.get_by_id(id)

    def get_by_column_name(self, column_name: str, value: str):
        return self.repo.get_by_column_name(column_name, value)

    def get_like_by_column_name(self, column_name: str, value: str):
        return self.repo.get_like_by_column_name(column_name, value)

    def delete_by_id(self, id: int):
        return self.repo.delete_by_id(id)

    def get_quantity_of_rown(self):
        return self.repo.get_quantity_of_rown()

    def put_in_table(self, id: int, data: dict):
        return self.repo.put_in_table(id, data)
