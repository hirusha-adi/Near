import asyncpg
from database.connection import psql_connection_async


@psql_connection_async()
async def dbget_embedError(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM embeds WHERE key LIKE 'error_%';")
        records = cursor.fetchall()
        cursor.close()

        # Convert records to dictionary
        data_dict = {}
        for record in records:
            key, value = record
            data_dict[key] = value

        return data_dict

    except (Exception, asyncpg.PostgresError) as error:
        print("Error while fetching data from 'general' table:", error)
