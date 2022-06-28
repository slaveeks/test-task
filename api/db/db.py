import psycopg2


class Db:
    """
    The Db gets data from database
    :param db_name - name of database
    :param db_user - username in databse
    :param db_password - database password
    :param db_host - host of database
    """
    def __init__(self, db_name, db_user, db_password, db_host):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host

    @staticmethod
    def close_cursor_and_connection(cur, conn):
        """
        Close db connection and cursor
        :param cur: cursor to close
        :param conn: connection to close
        """
        cur.close()
        conn.close()

    def get_db_connection(self):
        """
        Get db connection
        :return: database connection
        """
        conn = psycopg2.connect(dbname=self.db_name, user=self.db_user,
                                password=self.db_password, host=self.db_host)
        return conn

    def get_data_from_db(self):
        """
        Get all data from db
        :return: list
        """
        conn = self.get_db_connection()

        # Get cursor to work with db
        cur = conn.cursor()

        # Create select query
        select_query = '''SELECT * from GOOGLESHEET ORDER BY ID'''

        # Execute query
        cur.execute(select_query)

        # Fetch all data
        data = cur.fetchall()
        self.close_cursor_and_connection(cur, conn)

        return data

    def get_sum_of_price(self):
        conn = self.get_db_connection()

        # Get cursor to work with db
        cur = conn.cursor()

        # Create select query
        sum_select_query = ''' SELECT SUM ( USD_PRICE ) FROM GOOGLESHEET'''

        # Execute query
        cur.execute(sum_select_query)

        # Fetch the first data
        data = cur.fetchone()
        self.close_cursor_and_connection(cur, conn)

        return data[0]

    def get_ordered_data(self):
        conn = self.get_db_connection()

        # Get cursor to work with db
        cur = conn.cursor()

        # Create select query
        ordered_select_query = '''SELECT DELIVERY_TIME, SUM (USD_PRICE) from GOOGLESHEET
                                    GROUP BY DELIVERY_TIME
                                '''

        # Execute query
        cur.execute(ordered_select_query)

        # Get all data
        executed = cur.fetchall()

        # Create base for returning object
        res = {'labels': [],
               'values': []}

        # Parse every line of execution
        for line in executed:

            # Append executed data to object
            res['labels'].append(line[0])
            res['values'].append(line[1])

        self.close_cursor_and_connection(cur, conn)

        return res
