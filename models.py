
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from web import app


db = SQLAlchemy(app)

"""
To initiate, open a python shell and type:
    from alert import db
    db.create_all()
"""
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    confirmed = db.Column(db.Boolean(False))

    def __repr__(self):
        return '<%r>' % self.email
