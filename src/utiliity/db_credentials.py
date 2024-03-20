import os
from dotenv import load_dotenv

ENV = os.environ.get('ENV')
dotenv_path = '.env'

exists = os.path.exists(dotenv_path)

if not exists:
    raise Exception('env files does not exist')

load_dotenv(dotenv_path)

HOST = os.environ.get('DB_HOST')
USERNAME = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASS')
DATABASE = os.environ.get('DB_NAME')
PORT = int(os.environ.get('DB_PORT'))

credentials = {
    "DB_HOST": HOST,
    "DB_USER": USERNAME,
    "DB_PASS": PASSWORD,
    "DB_NAME": DATABASE,
    "DB_PORT": PORT,
}