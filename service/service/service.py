import time

from service.gs.gs import GoogleSheet
from service.db.db import Db
from service.cb.cb import Course
from service.telegram.telegram import Telegram

scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds_file = "creds.json"


class GoogleSheetService:
    def __init__(self):
        self.db = Db()
        self.gs = GoogleSheet()
        self.course = Course()
        self.tg = Telegram()
        self.elder_data = {}

    def schedule(self):
        while True:
            records = self.gs.get_all_records()
            self.db.check_remove(records)
            for i in records:
                if not i['№']:
                    continue
                i['стоимость,₽'] = "{:.2f}".format(self.course.get_usd_course() * i['стоимость,$'])
                if self.db.is_exists(i):
                    self.db.compare_data(i)
                else:
                    self.tg.telegram_bot_sendtext()
                    self.db.insert_data(i)
            time.sleep(5)

