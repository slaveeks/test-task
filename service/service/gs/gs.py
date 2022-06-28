import gspread
from oauth2client.service_account import ServiceAccountCredentials

# URLs for Google API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']


class GoogleSheet:
    """
    The GoogleSheet object helps to work with Google Sheets.
    :param creds_path: path of creds file for Google API
    :param document_name: name of document to parse
    """
    def __init__(self, creds_path, document_name):
        """
        Initialize class, make useful objects to work with Google API
        """

        # Parse creds
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path,
                                                                 scope)

        # Auth client
        client = gspread.authorize(creds)

        # Get sheet by document name
        self.sheet = client.open(document_name).sheet1

    def get_all_records(self):
        """
        Get all data from sheet
        :return: dict
        """
        return self.sheet.get_all_records()
