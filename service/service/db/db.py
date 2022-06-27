import psycopg2


class Db:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='postgres3', user='db_user',
                                password='mypassword', host='localhost', port="5432")
        self.cursor = self.conn.cursor()
        # SQL-запрос для создания новой таблицы
        create_table_query = '''CREATE TABLE GOOGLESHEET
                              (
                              ID     INT    NOT NULL UNIQUE ,
                              ORDER_NUMBER         INT  NOT NULL,
                              USD_PRICE  INT NOT NULL,
                              DELIVERY_TIME CHAR(10),
                              RUB_PRICE  REAL NOT NULL); '''
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insert_data(self, data):
        insert_query = """ INSERT INTO GOOGLESHEET (ID, ORDER_NUMBER, USD_PRICE, DELIVERY_TIME, RUB_PRICE)
         VALUES ({}, {}, {}, '{}', {})""".format(data['№'], data['заказ №'], data['стоимость,$'], data['срок поставки'], data['стоимость,₽'])
        self.cursor.execute(insert_query)
        self.conn.commit()

    def clear_table(self):
        clear_query = '''  TRUNCATE GOOGLESHEET; '''
        self.cursor.execute(clear_query)
        self.conn.commit()
