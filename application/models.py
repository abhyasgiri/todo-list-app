from application import db
from datetime import datetime

class Tasks(db.Model):
    id = db.column(db.Integer, primary_key=True)
    description = db.column(db.String(50), nullable=False)
    completed = db.column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

