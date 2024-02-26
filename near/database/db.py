import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "host": os.getenv("PSQL_HOST"),
    "user": os.getenv("PSQL_USER"),
    "password": os.getenv("PSQL_PASSWORD"),
    "database": os.getenv("PSQL_DATABASE"),
}


def connect_to_postgres():
    return psycopg2.connect(**CONFIG)


def postgres_connection(func):
    def wrapper(*args, **kwargs):
        connection = connect_to_postgres()
        try:
            result = func(connection, *args, **kwargs)
        except psycopg2.Error as error:
            print(f"Error occurred: {error}")
            result = None
        finally:
            if connection:
                connection.close()
        return result

    return wrapper


class Embeds:
    """
    postgres=# SELECT * FROM embeds;
     key                    | value
    ------------------------+-------
     common_color           | .....
     error_color            | .....
     error_description      | .....
     error_feild_name       | .....
     error_thumbnail        | .....
     error_title            | .....
     fakeinfo_color         | .....
     fakeinfo_thumbnail     | .....
     fakeinfo_title         | .....
     pleasewait_author_name | .....
     pleasewait_author_url  | .....
     pleasewait_color       | .....
     pleasewait_description | .....
     pleasewait_footer      | .....
     pleasewait_thumbnail   | .....
     pleasewait_title       | .....
    (16 rows)
    """

    @staticmethod
    @postgres_connection
    def add(connection, key, value):
        cursor = connection.cursor()
        sql_query = (
            "INSERT INTO embeds (key, value) VALUES (%s, %s) ON CONFLICT DO NOTHING"
        )
        cursor.execute(sql_query, (key, value))
        if cursor.rowcount == 1:  # dont re-insert if it already exists
            connection.commit()
            print("Key-value pair created successfully!")
        else:
            print("Key already exists. No insertion performed.")

    @staticmethod
    @postgres_connection
    def get(connection, key):
        cursor = connection.cursor()
        sql_query = "SELECT value FROM embeds WHERE key = %s"
        cursor.execute(sql_query, (key,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    @staticmethod
    @postgres_connection
    def update(connection, key, new_value):
        cursor = connection.cursor()
        sql_query = "UPDATE embeds SET value = %s WHERE key = %s"
        cursor.execute(sql_query, (new_value, key))
        connection.commit()
        print("Value updated successfully!")

    @staticmethod
    @postgres_connection
    def delete(connection, key):
        try:
            cursor = connection.cursor()
            sql_query = "DELETE FROM embeds WHERE key = %s"
            cursor.execute(sql_query, (key,))
            connection.commit()
            print("Key-value pair deleted successfully!")
        except psycopg2.Error as error:
            print("Failed to delete record from PostgreSQL table:", error)


def setup():

    def create_table_embed(cursor):
        """Create table if it does not exist"""
        cursor.execute(
            "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'embeds')"
        )
        table_exists = cursor.fetchone()[0]
        if not table_exists:
            cursor.execute(
                "CREATE TABLE embeds (key VARCHAR(255) PRIMARY KEY, value TEXT);"
            )
            print("Table 'Embeds' created successfully.")

    def setup_table_embed():
        """Load `embeds` table with defaults"""

        # pleasewait table
        Embeds.add("pleasewait_author_name", "NeaBot")
        Embeds.add(
            "pleasewait_author_url",
            "https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png",
        )
        Embeds.add("Pleasewait_title", "Please Wait")
        Embeds.add("pleasewait_description", "``` Processing Your Request ```")
        Embeds.add("pleasewait_color", "red")
        Embeds.add(
            "pleasewait_thumbnail",
            "https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif",
        )
        Embeds.add("pleasewait_footer", "Bot created by @hirushaadi")

        # error
        Embeds.add("error_title", "NeaBot")
        Embeds.add("error_description", "The command was unable to run successfully!")
        Embeds.add(
            "error_thumbnail",
            "https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png",
        )
        Embeds.add("error_feild_name", "Error:")
        Embeds.add("error_color", "red")

        # fake embeds for `near.cogs.fakeinfo`
        Embeds.add("fakeinfo_title", "Fake Information Generator")
        Embeds.add(
            "fakeinfo_thumbnail",
            "https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png",
        )
        Embeds.add("fakeinfo_color", "red")

        # common
        Embeds.add("common_color", "red")

    try:

        connection = connect_to_postgres()

        if connection:
            cursor = connection.cursor()
            create_table_embed(cursor=cursor)
            setup_table_embed()

    except psycopg2.Error as e:
        print("Error raised by PostgreSQL:", e)

    finally:
        # Close the connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")


if __name__ == "__main__":
    print(connect_to_postgres())
