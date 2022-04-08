from os import path

from flask_sqlalchemy import SQLAlchemy

from battleship.api import app

from boltfile import PROJECT_ROOT


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(PROJECT_ROOT, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True

db = SQLAlchemy()
