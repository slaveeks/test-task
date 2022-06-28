from datetime import date, datetime
import time

from service.gs.gs import GoogleSheet
from service.db.db import Db
from service.cb.cb import Course
from service.telegram.telegram import Telegram


class GoogleSheetService:
    """
    The GoogleSheetService for getting data from document
    and save it to database
    """

    def __init__(self):
        # Initiate Db class to save and get data
        self.db = Db()

        # Initiate GoogleSheet class to get data
        self.gs = GoogleSheet()

        # Initiate Course class to get current exchange rate
        self.course = Course()

        # Initiate Telegram class to send notifications
        self.tg = Telegram()

    def schedule(self):
        """
        Function to schedule parsing and checking Google sheet
        """

        # Infinite cycle
        while True:
            # Get records from Google sheet
            records = self.gs.get_all_records()
            # Check is saved to db data removed from table and remove it from db in this case
            self.db.check_deleted_data(records)

            # Cycle for every line in document
            for record in records:
                # Check is line data exists, if line is empty, skip this line
                if not record['№']:
                    continue

                # Create price in rubles, and pass it to object
                record['стоимость,₽'] = self.course.convert_from_usd_to_rub(record['стоимость,$'])

                # Check is record exists in db
                if self.db.is_exists(record):

                    # Compare record with saved data and update it, if there are any changes
                    self.db.compare_data_and_update(record)
                else:

                    # Insert new data to db
                    self.db.insert_data(record)

                    # Compare delivery time and today's date
                    if datetime.strptime(record['срок поставки'], '%d.%m.%Y').date() < date.today():

                        # Send notification about delivery delay
                        self.tg.telegram_bot_send_message('{} < {}'.format(record['срок поставки'], date.today()))
            # Scheduling delay
            time.sleep(5)

