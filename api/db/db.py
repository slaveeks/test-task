import psycopg2


class Db:
    def __init__(self):
        conn = psycopg2.connect(dbname='google_sheet', user='db_user',
                                password='mypassword', host='localhost')
        self.cursor = conn.cursor()

    def check_version(self):
        self.cursor.execute("SELECT version();")
