import secrets
from .main import db
from datetime import datetime

class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    location = db.Column(db.Unicode, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.creation_date = datetime.now()

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.Unicode, nullable=False)
    email = db.Column(db.Unicode, nullable=False)
    password = db.Column(db.Unicode, nullable=False)

    name = db.Column(db.Unicode, nullable=False)
    location = db.Column(db.Unicode, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """On construction, set date of creation."""
        super().__init__(*args, **kwargs)
        self.creation_date = datetime.now()
        self.token = secrets.token_urlsafe(64)