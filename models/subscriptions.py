"""
Using to define subscriptions and reference ...
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')


class subscriber(db.Model):
    """
    All data being storage on table "subscribers"

    id          | integer                        | not null
    
    email       | character varying(255)         | not null

    verify_code | character varying(255)         | not null

    verified_at | timestamp(0) without time zone | 

    created_at  | timestamp(0) without time zone | 

    updated_at  | timestamp(0) without time zone | 

    _global      | boolean                        | not null default true
    """

    __tablename__ = "subscribers"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    verify_code = db.Column(db.String(255), nullable=False)
    verified_at = db.Column(db.String(26))
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    # Igone error syntax, must be _global
    _global = db.Column(db.Boolean, default=True)


class subscription(db.Model):
    """
    All data being to storage on table "subscriptions"

    id            | integer                        | not null
    
    subscriber_id | integer                        | not null
    component_id  | integer                        | not null
    created_at    | timestamp(0) without time zone | 
    updated_at    | timestamp(0) without time zone |
    """

    __tablename__ = "subscriptions"

    id = db.Column(db.Integer, primary_key=True)
    subscriber_id = db.Column(db.Integer, nullable=False, index=True)
    component_id = db.Column(db.Integer, nullable=False, index=True)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)