from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@34.89.117.45/flask_db"
app.config["SECRET_KEY"] = "liabafeuhdanksllnksad"
db = SQLAlchemy(app)

from application import routes