import psycopg2


class Db:
    """
    The Db for working with database
    :param db_name: database name
    :param db_user: database user
    :param db_password: database passwort
    :param db_host: database host
    """
    def __init__(self, db_name, db_user, db_password, db_host):
        """
        Create database connection and create new table
        """

        # Connect to db
        self.conn = psycopg2.connect(dbname=db_name, user=db_user,
                                     password=db_password, host=db_host)

        # Get cursor
        self.cursor = self.conn.cursor()

        # Create query for creating table
        create_table_query = '''CREATE TABLE IF NOT EXISTS GOOGLESHEET (
                                     ID     INT   PRIMARY KEY,
                                     ORDER_NUMBER         INT  NOT NULL,
                                     USD_PRICE  INT NOT NULL,
                                     DELIVERY_TIME CHAR(10),
                                     RUB_PRICE  REAL NOT NULL); '''

        # Execute query
        self.cursor.execute(create_table_query)

        # Commit changes to db
        self.conn.commit()

    def insert_data(self, data):
        """
        Insert new data to db
        :param data: object to insert
        """

        # Create query for inserting new data to table
        insert_query = """ INSERT INTO GOOGLESHEET (ID, ORDER_NUMBER, USD_PRICE, DELIVERY_TIME, RUB_PRICE)
                                VALUES ({}, {}, {}, '{}', {})""".format(data['№'],
                                                                        data['заказ №'],
                                                                        data['стоимость,$'],
                                                                        data['срок поставки'],
                                                                        data['стоимость,₽'])
        # Execute query
        self.cursor.execute(insert_query)

        # Commit changes to db
        self.conn.commit()

    def is_exists(self, data):
        """
        Check is incoming data exists in table
        :param data: data to check
        :return: boolean
        """

        # Create query for select data by id
        select_query = ''' SELECT 1 FROM GOOGLESHEET WHERE ID={}'''.format(data['№'])

        # Execute query
        self.cursor.execute(select_query)

        # Check length of returned data
        if len(self.cursor.fetchall()) == 0:
            return False
        else:
            return True

    def compare_data_and_update(self, data):
        """
        Compare incoming and saved data, if there are some changes, table updates
        :param data: incoming data to compare
        :return:
        """

        # Create select data query
        select_query = ''' SELECT * FROM GOOGLESHEET WHERE ID={}'''.format(data['№'])

        # Execute query
        self.cursor.execute(select_query)

        # Get the first element of returned data, because id is unique
        db_data = self.cursor.fetchall()[0]

        # Create object and parse db data like incoming data
        elder_data = {
            '№': db_data[0],
            'заказ №': db_data[1],
            'стоимость,$': db_data[2],
            'срок поставки': db_data[3],
            'стоимость,₽': db_data[4],
        }

        # Compare incoming and saved data
        if data == elder_data:

            # If they are the same, do nothing
            return

        # Create update query
        update_query = ''' UPDATE GOOGLESHEET
         SET  ORDER_NUMBER={}, USD_PRICE={}, 
         DELIVERY_TIME='{}', RUB_PRICE={} WHERE ID={}'''.format(data['заказ №'],
                                                                data['стоимость,$'],
                                                                data['срок поставки'],
                                                                data['стоимость,₽'],
                                                                data['№'])

        # Execute query
        self.cursor.execute(update_query)

        # Commit changes to db
        self.conn.commit()

    def get_all_id_from_db(self):
        """
        Get all id from table
        :return: lict
        """

        # Create select query
        select_query = ''' SELECT ID FROM GOOGLESHEET '''

        # Execute query
        self.cursor.execute(select_query)

        # Get all returned data
        data = self.cursor.fetchall()

        return data

    def check_deleted_data(self, data):
        """
        Check is data delete and remove it from db
        :param data: incoming data to check
        :return:
        """

        # Get returned from db data with id
        id_arr = self.get_all_id_from_db()

        for element in id_arr:
            # Every element has this structure: ({int},), check is db id exists in incoming data
            res = next((item for item in data if item["№"] == element[0]), None)

            # Check res contains any data
            if not res:

                # Create query to delete removed from Google Docs data from db
                delete_query = ''' DELETE FROM GOOGLESHEET WHERE ID={}'''.format(element[0])

                # Execute query
                self.cursor.execute(delete_query)

                # Commit changes
                self.conn.commit()
