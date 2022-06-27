import psycopg2


class Db:
    def get_db_connection(self):
        conn = psycopg2.connect(dbname='postgres3', user='db_user',
                                password='mypassword', host='localhost')
        return conn

    def check_version(self):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        cur.close()
        conn.close()

    def get_data_from_db(self):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute('''SELECT * from GOOGLESHEET ORDER BY ID''')
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def get_sum_of_price(self):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute(''' SELECT SUM ( USD_PRICE ) FROM GOOGLESHEET''')
        data = cur.fetchone()
        print(data)
        cur.close()
        conn.close()
        return data[0]

    def get_ordered_data(self):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute('''SELECT DELIVERY_TIME, SUM (USD_PRICE) from GOOGLESHEET
                      GROUP BY DELIVERY_TIME
                                ''')
        executed = cur.fetchall()
        arr = { 'labels': [],
                'values': []}
        print(executed)
        for line in executed:
            arr['labels'].append(line[0])
            arr['values'].append(line[1])
        cur.close()
        conn.close()
        return arr
