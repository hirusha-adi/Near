import os
import psycopg2
import asyncpg


def psql_connection():
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                connection = psycopg2.connect(
                    user=os.getenv("PSQL_USER"),
                    password=os.getenv("PSQL_PASSWORD"),
                    host=os.getenv("PSQL_HOST"),
                    database=os.getenv("PSQL_DATABASE"),
                )
                result = func(connection, *args, **kwargs)
                connection.close()
                return result
            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL:", error)

        return wrapper

    return decorator


def psql_connection_async():
    async def decorator(func):
        async def wrapper(*args, **kwargs):
            try:
                connection = await asyncpg.connect(
                    user=os.getenv("PSQL_USER"),
                    password=os.getenv("PSQL_PASSWORD"),
                    host=os.getenv("PSQL_HOST"),
                    database=os.getenv("PSQL_DATABASE"),
                )
                result = await func(connection, *args, **kwargs)
                await connection.close()
                return result
            except (Exception, asyncpg.PostgresError) as error:
                print("Error while connecting to PostgreSQL:", error)

        return wrapper

    return decorator
