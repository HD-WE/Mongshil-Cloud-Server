# config server 
import os

db = {
    'user'     : 'root',
    'password' : '[your password]',
    'host'     : '127.0.0.1',
    'port'     : '3306',
    'database' : 'mungshil_cloud_db'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8" 

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", '[google id]')
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", '[google secret]')