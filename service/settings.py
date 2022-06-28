import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.', '.env')
load_dotenv(dotenv_path)

DB_NAME = os.environ.get('DB_NAME')

DB_USER = os.environ.get('DB_USER')

DB_PASSWORD = os.environ.get('DB_PASSWORD')

DB_HOST = os.environ.get('DB_HOST')

SCHEDULING_DELAY = int(os.environ.get('SCHEDULING_DELAY'))

DOCUMENT_NAME = os.environ.get('DOCUMENT_NAME')

CREDS_PATH = os.environ.get('CREDS_PATH')

CURRENCY_ID = os.environ.get('CURRENCY_ID')

CB_API_URL = os.environ.get('CB_API_URL')

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

TELEGRAM_API_URL = os.environ.get('TELEGRAM_API_URL')
