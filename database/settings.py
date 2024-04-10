import psycopg2
from database.connection import psql_connection


@psql_connection()
def dbget_mainSettings(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM general;")
        records = cursor.fetchall()
        cursor.close()

        # Convert records to dictionary
        data_dict = {}
        for record in records:
            key, value = record
            data_dict[key] = value

        return data_dict

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from 'general' table:", error)
