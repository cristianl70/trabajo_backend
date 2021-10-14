from decouple import config
from pymongo import MongoClient

MONGO_HOST = config('MONGO_HOST', default='mongo')
MONGO_PORT = config('MONGO_PORT', default='27017')
MONGO_USER= config('MONGO_INITDB_ROOT_USERNAME', default='root')
MONGO_PASSWORD = config('MONGO_INITDB_ROOT_PASSWORD', default='password')

def get_connection():
    return MongoClient(
        host = f'{MONGO_HOST}:{MONGO_PORT}',
        username=MONGO_USER,
        password=MONGO_PASSWORD
    )
