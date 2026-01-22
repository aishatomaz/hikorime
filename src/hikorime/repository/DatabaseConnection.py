import sqlite3

class RepositoryConnection:
    """
        Connects to the database, and make pure sql querys
    """

    def __init__(self):
        print("Verifing database...")

        # TODO Verify database
        
        print("Database is ready!")

    def newQuery(self, query: str,  data: dict | None = None):

        connect = sqlite3.connect("../repoTest.db") # .. = parent directory
        cursor = connect.cursor()
        # session = self._SessionLocal()
        try:
            # Execute 'Select' querys
            if query.strip().upper().startswith("SELECT"):
                result = cursor.execute(query, data)
                return result
            
            # Execute update, insert and delete
            if data is not None:
                # Execute the query and the data params
                cursor.execute(query, data)
            else:
                # Execute the query
                cursor.execute((query)) # Don't know what query, but is good to have i think

            connect.commit()
            print("CHANGES MADE WITH SUCESS")

        except Exception as error:
            print(f"error - {error} doing rollback")
            connect.rollback() # GOTO the last state before the query
            return None

        finally:
            cursor.close()
            print("CONNECTION CLOSED")
