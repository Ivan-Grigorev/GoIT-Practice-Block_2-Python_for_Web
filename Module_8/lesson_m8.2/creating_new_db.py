import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def creating_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="v320",
                                      host="127.0.0.1",
                                      port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = connection.cursor()
        sql_create_database = 'create database test_db'
        cursor.execute(sql_create_database)
        print('DB has been created')
    except (Exception, Error) as error:
        print("Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection Closed")


def creating_inserting_to_db():
    try:

        connection = psycopg2.connect(user="postgres",
                                      password="v320",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test_db")

        cursor = connection.cursor()
        create_query = """CREATE TABLE phone
                          (ID INT PRIMARY KEY     NOT NULL,
                          MODEL           TEXT    NOT NULL,
                          PRICE         INT   NOT NULL); """

        cursor.execute(create_query)
        connection.commit()
        print("Successfully created table Phone at PostgreSQL")
        insert_query = """ INSERT INTO phone (ID, MODEL, PRICE)
                                           VALUES (%s,%s,%s)"""
        record_to_insert = (1, 'Iphone X', 950)
        cursor.execute(insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, f"Record successfully added to table Phone")
    except (Exception, Error) as error:
        print("Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection closed")


def update_table(mobile_id, price):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="v320",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test_db")

        cursor = connection.cursor()
        print("Table BEFORE updating")
        select_query = """select * from phone where id = %s"""
        cursor.execute(select_query, (mobile_id,))
        record = cursor.fetchone()
        print(record)

        # Обновление отдельной записи
        update_query = """Update phone set price = %s where id = %s"""
        cursor.execute(update_query, (price, mobile_id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record has been successfully updated")

        print("Table AFTER updating")
        select_query = """select * from phone where id = %s"""
        cursor.execute(select_query, (mobile_id,))
        record = cursor.fetchone()
        print(record)
    except (Exception, Error) as error:
        print("Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection closed")


def delete_data(mobile_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="v320",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="test_db")

        cursor = connection.cursor()
        delete_query = """Delete from  phone where id = %s"""
        cursor.execute(delete_query, (mobile_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Successfully deleted")
    except (Exception, Error) as error:
        print("Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection Closed")


def delete_table():
    with psycopg2.connect(user="postgres",
                          password="v320",
                          host="127.0.0.1",
                          port="5432",
                          database="test_db") as connection:
        with connection.cursor() as cursor:
            cursor.execute("Drop table phone")

    print('Successfully deleted')


if __name__ == '__main__':
    creating_db()
    creating_inserting_to_db()
    update_table(1, 750)
    delete_data(1)
    delete_table()
