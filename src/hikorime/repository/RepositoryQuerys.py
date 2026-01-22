from hikorime.repository.RepositoryConnection import RepositoryConnection

from datetime import date

class repositoryQuerys:

    def __init__(self, table_name: str):
        self.bookshelf = table_name

    def save(
        self, title, author, year, genre, pages_number, avaliation=None, edition=None
    ):
        data = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "inclusion_date": date.today(),
            "pages_number": pages_number,
            "avaliation": avaliation
        }

        if edition is not None:
            data.update({"edition": edition})
            query = f"""
                INSERT INTO {self.bookshelf}
                (title, author, year, type, inclusion_date, genre, pages_number, avaliation, edition, status)
                VALUES (:title, :author, :year, 'MAGAZINE', :inclusion_date, :genre, :pages_number, :avaliation, :edition, 'unread');
            """
        else:
            query = f"""
                INSERT INTO {self.bookshelf}
                (title, author, year, type, inclusion_date, genre, pages_number, avaliation, status)
                VALUES (:title, :author, :year, 'BOOK', :inclusion_date, :genre, :pages_number, :avaliation, 'unread');
            """

        return RepositoryConnection().newQuery(query, data)
        
    def getAll(self):
        """
        debug only
        
        :return: all in the table
        """

        query = f"select * from {self.bookshelf};"

        return RepositoryConnection().newQuery(query)
    
    def getById(self, id: int):
        data = ({"id": id})

        query = f"select * from {self.bookshelf} where id = :id;"

        return RepositoryConnection().newQuery(query, data)
    
    def getByColumnName(self, column_name:str, value:str):
        """
        Return a query of the column name and its values 

        Args:
            column_name: the column name (ex: title, genre)
            value: all the data that will be selected
        """

        if not column_name.isidentifier():
            raise ValueError(f"Invalid column name: {column_name}")

        data = {"value": value}

        query = f"""SELECT * FROM {self.bookshelf} WHERE {column_name} = :value;"""

        return RepositoryConnection().newQuery(query, data)
    
    def getLikeByColumnName(self, column_name: str, value: str):
        """
        Return a query of the column name and its values

        Args:
            column_name: the column name (ex: title, genre)
            value: all the data that will be selected
        """

        if not column_name.isidentifier():
            raise ValueError(f"Invalid column name: {column_name}")

        data = {"value": f"%{value}%"} # I like the like operation (:

        query = f"""SELECT * FROM {self.bookshelf} WHERE {column_name} LIKE :value;"""

        return RepositoryConnection().newQuery(query, data)


    def deleteById(self, id:int):
        data = ({"id": id})

        query = f"DELETE FROM {self.bookshelf} WHERE id=:id;"

        return RepositoryConnection().newQuery(query, data)
    
    def getBestFivePublications(self):
        query = f"SELECT title, avaliation FROM {self.bookshelf} ORDER BY avaliation DESC LIMIT 5;"

        return RepositoryConnection().newQuery(query)
    
    def getCompletedAverageScore(self):
        query = f"SELECT title, avaliation FROM {self.bookshelf};"

        return RepositoryConnection().newQuery(query)

    def getPublicationAmount(self):
        query = f"SELECT COUNT(id) FROM {self.bookshelf};"

        return RepositoryConnection().newQuery(query)

    def putPublication(self, id: int, data: dict):
        queries = []
        params = []

        for key, value in data.items():
            if value is None:
                continue

            queries.append(f"UPDATE {self.bookshelf} SET {key} = :value WHERE id = :id")
            params.append({"id": id, "value": value})

        repo = RepositoryConnection()

        for query, param in zip(queries, params):
            repo.newQuery(query, param)
