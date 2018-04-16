"""
Using to defined jobs
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')

class job(db.Model):
    """
    All data being storage on table "jobs"

    id           | bigint                 | not null

    queue        | character varying(255) | not null

    payload      | text                   | not null

    attempts     | smallint               | not null

    reserved     | smallint               | not null

    reserved_at  | integer                | 

    available_at | integer                | not null

    created_at   | integer                | not null
    """
    
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    queue = db.Column(db.String(255), nullable=False)
    payload = db.Column(db.Text, nullable=False)
    attempts = db.Column(db.Integer, nullable=False)
    reversed = db.Column(db.Integer, nullable=False)
    reserved_at = db.Column(db.String(26), nullable=False)
    available_at = db.Column(db.String(26), nullable=False)
    created_at = db.Column(db.String(26), default=now)

class failed_job(db.Model):
    """
    All data being storage on table "failed_jobs"

    id         | integer                        | not null default

    connection | text                           | not null

    queue      | text                           | not null

    payload    | text                           | not null

    failed_at  | timestamp(0) without time zone | not null
    """

    __tablename__ = "failed_jobs"

    id = db.Column(db.Integer, primary_key=True)
    connection = db.Column(db.Text, nullable=False)
    queue = db.Column(db.Text, nullable=False)
    payload = db.Column(db.Text, nullable=False)
    failed_at = db.Column(db.String(26), nullable=False)