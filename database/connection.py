import os
import psycopg2
from psycopg2 import Error

def psql_connection():
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                connection = psycopg2.connect(
                    user=os.getenv("PSQL_USER"),
                    password=os.getenv("PSQL_PASSWORD"),
                    host=os.getenv("PSQL_HOST"),
                    database=os.getenv("PSQL_DATABASE")
                )
                result = func(connection, *args, **kwargs)
                connection.close()
                return result
            except (Exception, Error) as error:
                print("Error while connecting to PostgreSQL:", error)
        return wrapper
    return decorator
