import os

class Config:
    SECRET_KEY = os.urandom(32)
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Hella123,'
    MYSQL_DB = 'ferremas'
    MYSQL_HOST = 'localhost'
    port=3306

