from .main import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    # Coodinates/address?
    address = db.Column(db.Unicode, nullable=False)
    # Buyer or Seller
    user_type = db.Column(db.Unicode, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """On construction, set date of creation."""
        super().__init__(*args, **kwargs)
        self.creation_date = datetime.now()
