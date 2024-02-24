import mysql.connector

CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "nearbot_dev"
}

def connect_to_mysql():
    return mysql.connector.connect(**CONFIG)

def mysql_connection(func):
    def wrapper(*args, **kwargs):
        connection = connect_to_mysql()
        try:
            result = func(connection, *args, **kwargs)
        except mysql.connector.Error as error:
            print(f"Error occurred: {error}")
            result = None
        finally:
            if connection.is_connected():
                connection.close()
        return result
    return wrapper

class Embeds:
    """
    mysql> SELECT * FROM embeds;
    +------------------------+-------+
    | key                    | value |
    +------------------------+-------+
    | error_color            | ..... |
    | error_description      | ..... |
    | error_feild_name       | ..... |
    | error_thumbnail        | ..... |
    | error_title            | ..... |
    | fakeinfo_color         | ..... |
    | fakeinfo_thumbnail     | ..... |
    | fakeinfo_title         | ..... |
    | pleasewait_author_name | ..... |
    | Pleasewait_author_url  | ..... |
    | pleasewait_color       | ..... |
    | Pleasewait_description | ..... |
    | pleasewait_footer      | ..... |
    | pleasewait_thumbnail   | ..... |
    | Pleasewait_title       | ..... |
    +------------------------+-------+
    16 rows in set (0.00 sec)
    """
    @staticmethod
    @mysql_connection
    def add(connection, key, value):
        cursor = connection.cursor()
        sql_query = "INSERT IGNORE INTO embeds (`key`, `value`) VALUES (%s, %s)"
        cursor.execute(sql_query, (key, value))
        if cursor.rowcount == 1: # dont re-insert if it already exists
            connection.commit()
            print("Key-value pair created successfully!")
        else:
            print("Key already exists. No insertion performed.")

    @staticmethod
    @mysql_connection
    def get(connection, key):
        cursor = connection.cursor()
        sql_query = "SELECT `value` FROM embeds WHERE `key` = %s"
        cursor.execute(sql_query, (key,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    @staticmethod
    @mysql_connection
    def update(connection, key, new_value):
        cursor = connection.cursor()
        sql_query = "UPDATE embeds SET `value` = %s WHERE `key` = %s"
        cursor.execute(sql_query, (new_value, key))
        connection.commit()
        print("Value updated successfully!")
    
    @staticmethod
    @mysql_connection
    def delete(connection, key):
        try:
            cursor = connection.cursor()
            sql_query = "DELETE FROM embeds WHERE `key` = %s"
            cursor.execute(sql_query, (key,))
            connection.commit()
            print("Key-value pair deleted successfully!")
        except mysql.connector.Error as error:
            print("Failed to delete record from MySQL table:", error)

def setup():
    
    def create_table_embed(cursor):
        """Create table if it does not exist"""
        cursor.execute("SHOW TABLES LIKE 'Embeds'")
        table_exists = cursor.fetchone()
        if not table_exists:
            cursor.execute("CREATE TABLE embeds (`key` VARCHAR(255) PRIMARY KEY, `value` TEXT);")
            print("Table 'Embeds' created successfully.")
    
    def setup_table_embed():
        """Load `embeds` table with defaults"""
        
        # pleasewait table
        Embeds.add("pleasewait_author_name", "NeaBot")
        Embeds.add("Pleasewait_author_url", "https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        Embeds.add("Pleasewait_title", "Please Wait")
        Embeds.add("Pleasewait_description", "``` Processing Your Request ```")
        Embeds.add("pleasewait_color", "red")
        Embeds.add("pleasewait_thumbnail", "https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
        Embeds.add("pleasewait_footer", "Bot created by @hirushaadi")
        
        # error
        Embeds.add("error_title", "NeaBot")
        Embeds.add("error_description", "The command was unable to run successfully!")
        Embeds.add("error_thumbnail", "https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        Embeds.add("error_feild_name", "Error:")
        Embeds.add("error_color", "red")
        
        # fake embeds for `near.cogs.fakeinfo`
        Embeds.add("fakeinfo_title", "Fake Information Generator")
        Embeds.add("fakeinfo_thumbnail", "https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        Embeds.add("fakeinfo_color", "red")
        
        # common
        Embeds.add("common_color", "red")
        
    try:
        
        connection = connect_to_mysql()

        if connection.is_connected():
            cursor = connection.cursor()
            create_table_embed(cursor=cursor)
            setup_table_embed()

    except mysql.connector.Error as e:
        print("Error raised by MySQL:", e)
    
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")
        