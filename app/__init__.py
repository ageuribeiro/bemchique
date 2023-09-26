from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = '611b32d89900b8a1c215b64cfa212fdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bemchique.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
