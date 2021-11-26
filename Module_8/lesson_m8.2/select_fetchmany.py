import psycopg2
from psycopg2 import Error


try:    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",  # пароль, который указали при установке PostgreSQL
                                  password="v320",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Computer Firm")

    cursor = connection.cursor()
    postgresql_select_query = "select * from product"

    cursor.execute(postgresql_select_query)
    product_records = cursor.fetchmany(2)

    print("Selecting two records")
    for row in product_records:
        print("maker=", row[0], )
        print("model =", row[1])
        print("type =", row[2], "\n")

    product_records = cursor.fetchmany(10)

    print("Selecting next ten records")
    for row in product_records:
        print("maker =", row[0], )
        print("model =", row[1])
        print("type=", row[2], "\n")
except (Exception, Error) as error:
    print("Error while working with PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed")
