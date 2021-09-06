from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/db_finkargo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
auth = HTTPBasicAuth()

db= SQLAlchemy(app)

from views import *
from models import *
