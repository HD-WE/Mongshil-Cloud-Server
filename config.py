# config server 
db = {
    'user'     : 'root',
    'password' : 'm-s-j-0-1-3-0',
    'host'     : '127.0.0.1',
    'port'     : '3306',
    'database' : 'mungshil_cloud_db'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8" 