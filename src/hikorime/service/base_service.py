from hikorime.repository.repository_querys import RepositoryQuerys


class BaseService:
    """
    Classe base para outras classes do tipo servico
    Lembre de fazer a funcao save para cada service individualmente
    """

    def __init__(self, repository: RepositoryQuerys):
        self.repo = repository

    # Devido as divergencias, def save sera feito por service

    def get_all(self):
        """
        Retorna todos as linhas de uma tabela (não use em operacao)
        """
        return self.repo.get_all()

    def get_by_id(self, id: int):
        """
        Retorn uma linha com o id especifico
        """
        return self.repo.get_by_id(id)

    def get_by_column_name(self, column_name: str, value: str):
        """
        Retorna o(s) valor(es) exato(s) de uma coluna especifica
        ARGS:
            column_name: O nome da coluna da tabela a ser buscado
            value: o valor exato que quer buscar
        """
        return self.repo.get_by_column_name(column_name, value)

    def get_like_by_column_name(self, column_name: str, value: str):
        """
        Retorna o(s) valor(es) parciais(s) de uma coluna especifica
        ARGS:
            column_name: O nome da coluna da tabela a ser buscado
            value: o valor parcial que quer buscar (se precisar de um valor exato, use get_by_column_name)
        EX:
            column_name = nome
            value = invers
            ira retorna, por exemplo, invers, invers-sama, etc
        """
        return self.repo.get_like_by_column_name(column_name, value)

    def delete_by_id(self, id: int):
        """
        Deleta uma linha  usando seu id
        """
        return self.repo.delete_by_id(id)

    def get_quantity_of_rown(self):
        """
        retorna a quantidade de linhas de uma coluna
        """
        return self.repo.get_quantity_of_rown()

    def put_in_table(self, id: int, data: dict):
        """
        Um put, vai apenas mudar uma coluna da linha da tabela
        exemplo, posso mudar 'invers' para 'sudo invers', sem alterar qualquer outro dado dele.
        ARGS:
            id: o id da linha que queira mudar
            data: o dict que vai fazer as mudancas, recomendo ver o exemplo de funcionamento abaixo
        EX:

        """
        return self.repo.put_in_table(id, data)
