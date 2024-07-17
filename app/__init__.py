
from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS 
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)
CORS(app)

cors = CORS(app, resource={
   r"/api/v1/transbank/*":{
        "origins":"*"
    }
})
from .routes import *
