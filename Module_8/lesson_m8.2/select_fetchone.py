import psycopg2
from psycopg2 import Error


try:  # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",  # пароль, который указали при установке PostgreSQL
                                  password="v320",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Computer Firm")

    cursor = connection.cursor()
    postgresql_select_query = "select * from laptop"

    cursor.execute(postgresql_select_query)

    laptop_records_one = cursor.fetchone()
    print("Displaying the first record", laptop_records_one)

    laptop_records_two = cursor.fetchone()
    print("Displaying the second record", laptop_records_two)

except (Exception, Error) as error:
    print("Error while working with PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")
