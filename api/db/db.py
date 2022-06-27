import psycopg2


class Db:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='postgres3', user='db_user',
                                password='mypassword', host='localhost')
        self.cursor = self.conn.cursor()

    def check_version(self):
        self.cursor.execute("SELECT version();")

    def get_data_from_db(self):
        self.cursor.execute('''SELECT * from GOOGLESHEET''')
        data = self.cursor.fetchall()
        print(data)
        self.conn.commit()
        return data

    def get_sum_of_price(self):
        self.cursor.execute(''' SELECT SUM ( USD_PRICE ) FROM GOOGLESHEET''')
        data = self.cursor.fetchone()
        print(data)
        self.conn.commit()
        return data[0]

    def get_ordered_data(self):
        self.cursor.execute('''SELECT DELIVERY_TIME, SUM (RUB_PRICE) from GOOGLESHEET
                                GROUP BY DELIVERY_TIME ''')
        executed = self.cursor.fetchall()
        arr = { 'labels': [],
                'values': []}
        for line in executed:
            arr['labels'].append(line[0])
            arr['values'].append(line[1])
        print(arr)
        self.conn.commit()
        return arr
