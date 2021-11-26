import psycopg2
from psycopg2 import DatabaseError


try:
    connection = psycopg2.connect(user="postgres",
                                  password="v320",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Computer Firm 2")

    connection.autocommit = False
    cursor = connection.cursor()
    amount = 200

    query = """select price from pc where code = 1"""
    cursor.execute(query)
    record = cursor.fetchone()[0]
    price_a = int(record)
    price_a -= amount

    sql_update_query = """update pc set price = %s where code = 1"""
    cursor.execute(sql_update_query, (price_a,))

    amount_x = 'asfdfs'
    query = """select price from pc where code = 2"""
    cursor.execute(query)
    record = cursor.fetchone()[0]
    price_b = int(record)
    price_b += amount_x

    sql_update_query = """Update pc set price = %s where code = 2"""
    cursor.execute(sql_update_query, (price_b,))

    # совершение транзакции
    connection.commit()
    print("Transaction ended")

except (Exception, psycopg2.DatabaseError) as error:
    print("Transaction error. Cancel all transaction operations.", error)
    connection.rollback()
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")
