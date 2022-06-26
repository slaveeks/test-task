import psycopg2


class Db:
    def __init__(self):
        conn = psycopg2.connect(dbname='postgres3', user='db_user',
                                password='mypassword', host='localhost')
        self.cursor = conn.cursor()

    def check_version(self):
        self.cursor.execute("SELECT version();")

    def get_data_from_db(self):
        self.cursor.execute('''SELECT * from GOOGLESHEET ORDER BY DELIVERY_TIME''')
        return self.cursor.fetchall()

    def get_sum_of_price(self):
        self.cursor.execute(''' SELECT SUM ( USD_PRICE ) FROM GOOGLESHEET''')
        return self.cursor.fetchone()[0]
