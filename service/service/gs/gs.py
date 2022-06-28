import gspread
from oauth2client.service_account import ServiceAccountCredentials

# URLs for Google API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']

# Path for file with creds for Google API
creds_file = 'creds.json'


class GoogleSheet:
    """The GoogleSheet object helps to work with Google Sheets."""
    def __init__(self):
        """
        Initialize class, make useful objects to work with Google API
        """

        # Parse creds
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file,
                                                                 scope)

        # Auth client
        client = gspread.authorize(creds)

        # Get sheet by document name
        self.sheet = client.open('Тестовое задание').sheet1

    def get_all_records(self):
        """
        Get all data from sheet
        :return: dict
        """
        return self.sheet.get_all_records()
