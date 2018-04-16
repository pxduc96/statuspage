"""
Using to define a object invited
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')

class invite(db.Model):
    """
    All data being storage on table "invites"

    id         | integer                        | not null

    code       | character varying(255)         | not null

    email      | character varying(255)         | not null

    claimed_at | timestamp(0) without time zone | 

    created_at | timestamp(0) without time zone | 

    updated_at | timestamp(0) without time zone |
    """

    __tablename__ = "invites"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    claimed_at = db.Column(db.String(26))
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
