from flask import Flask
from flask_sqlalchemy import SQLalchemy

app == Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@34.89.117.45/flask_db"

db = SQLalchemy(app)

 