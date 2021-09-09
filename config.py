# config server 
db = {
    'user'     : 'root',
    'password' : '[password]',
    'host'     : '127.0.0.1',
    'port'     : '3306',
    'database' : 'Mungshil-Cloud-DB'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8" 