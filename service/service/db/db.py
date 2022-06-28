import psycopg2


class Db:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='postgres3', user='db_user',
                                password='mypassword', host='localhost', port="5432")
        self.cursor = self.conn.cursor()
        create_table_query = '''CREATE TABLE GOOGLESHEET
                              (
                              ID     INT   PRIMARY KEY,
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

    def is_exists(self, data):
        self.cursor.execute(''' SELECT 1 FROM GOOGLESHEET WHERE ID={}'''.format(data['№']))
        if len(self.cursor.fetchall()) == 0:
            return False
        else:
            return True

    def compare_data(self, data):
        self.cursor.execute(''' SELECT * FROM GOOGLESHEET WHERE ID={}'''.format(data['№']))
        db_data = self.cursor.fetchall()[0]
        elder_data = {
            '№': db_data[0],
            'заказ №': db_data[1],
            'стоимость,$': db_data[2],
            'срок поставки': db_data[3],
            'стоимость,₽': db_data[4],
        }
        if data == elder_data:
            return
        self.cursor.execute(''' UPDATE GOOGLESHEET SET  ORDER_NUMBER={}, USD_PRICE={}, DELIVERY_TIME='{}', RUB_PRICE={} WHERE ID={}'''.format(data['заказ №'], data['стоимость,$'], data['срок поставки'], data['стоимость,₽'], data['№']))
        self.conn.commit()

    def get_ids(self):
        self.cursor.execute(''' SELECT ID FROM GOOGLESHEET ''')
        data = self.cursor.fetchall()
        return data

    def check_remove(self, data):
        ids = self.get_ids()
        for id in ids:
            res = next((item for item in data if item["№"] == id[0]), None)
            if not res:
                self.cursor.execute(''' DELETE FROM GOOGLESHEET WHERE ID={}'''.format(id[0]))
