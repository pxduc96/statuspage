"""
Using to define reference with metrics
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')


class metric(db.Model):
    """
    All data being storage on table "metrics"

    id            | integer                        | not null

    name          | character varying(255)         | not null

    suffix        | character varying(255)         | not null

    description   | text                           | not null

    default_value | numeric(10,3)                  | not null

    calc_type     | smallint                       | not null

    display_chart | boolean                        | not null default true

    created_at    | timestamp(0) without time zone | 

    updated_at    | timestamp(0) without time zone | 

    places        | integer                        | not null default 2

    default_view  | Boolean                       | not null default True

    threshold     | integer                        | not null default 5

    order         | smallint                       | not null default '0'::smallint
    """

    __tablename__ = "metrics"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    suffix = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    default_value = db.Column(db.Integer, nullable=False)
    calc_type = db.Column(db.Integer, nullable=False)
    display_chart = db.Column(db.Boolean, default=True, index=True)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    places = db.Column(db.Integer, default=2)
    default_view = db.Column(db.Boolean, default=True)
    threshold = db.Column(db.Integer, default=5)
    order = db.Column(db.Integer, default=0)


class metric_point(db.Model):
    """
    All data being storage on table "metric_points"

    id         | integer                        | not null
    
    metric_id  | integer                        | not null

    value      | numeric(15,3)                  | not null

    created_at | timestamp(0) without time zone | 

    updated_at | timestamp(0) without time zone | 

    counter    | integer                        | not null default 1
    """

    __tablename__ = "metric_points"

    id = db.Column(db.Integer, primary_key=True)
    metric_id = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    counter = db.Column(db.Integer, default=1)