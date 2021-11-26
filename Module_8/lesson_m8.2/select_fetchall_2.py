import psycopg2
from psycopg2 import Error


def get_printer_info(printer_code):
    try:
        connection = psycopg2.connect(user="postgres",

                                      password="v320",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="Computer Firm")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from printer where code = '%s'"

        cursor.execute(postgreSQL_select_Query, (printer_code,))
        print("Taking all records", '\n')
        printer_records = cursor.fetchall()

        print("Print each record", '\n')
        for row in printer_records:
            print("color =", row[2], )
            print("type =", row[3])
            print("price =", row[4], "\n")
    except (Exception, Error) as error:
        print("Error while working with PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection closed")


if __name__ == '__main__':
    get_printer_info(4)
    get_printer_info(5)
