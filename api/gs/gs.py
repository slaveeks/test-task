import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds_file = "creds.json"


class GoogleSheet:
    """The GoogleSheet object helps to work with Google Sheets."""
    def __int__(self):
        """
        Initialize class, make useful objects to work with Google API
        """
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file,
                                                                 scope)
        client = gspread.authorize(creds)
        self.sheet = client.open("Тестовое задание").sheet1

    def get_all_records(self):
        """
        Get all data from sheet
        :return: dict
        """
        return dict(self.sheet.get_all_records())
