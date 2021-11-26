import psycopg2
from psycopg2 import Error


try:
    connection = psycopg2.connect(user="postgres",
                                  password="pstgr_28.09_ig",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="module_8.hw")

    cursor = connection.cursor()

    print("Information about PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")

    cursor.execute("SELECT version();")

    record = cursor.fetchone()
    print("You are connected to -", record, "\n")
except (Exception, Error) as error:
    print("Error", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")
