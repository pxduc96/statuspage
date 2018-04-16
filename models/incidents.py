"""
Using define a incidents
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')

class incident(db.Model):
    """
    All data being storage on table "incidents"
    
    id           | integer                        | not null

    component_id | integer                        | not null default 0

    name         | character varying(255)         | not null

    status       | integer                        | not null

    message      | text                           | not null

    created_at   | timestamp(0) without time zone |

    updated_at   | timestamp(0) without time zone | 

    deleted_at   | timestamp(0) without time zone | 

    scheduled_at | timestamp(0) without time zone | 

    visible      | boolean                        | not null default true
    """
    __tablename__ = "incidents"

    id = db.Column(db.Integer, primary_key=True)
    component_id = db.Column(db.Integer, default=0, index=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False, index=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.String(26), default=now)
    update_at = db.Column(db.String(26), default=now)
    delete_at = db.Column(db.String(26), default="null")
    scheduled_at = db.Column(db.String(26), default="null")
    visible = db.Column(db.Boolean, default=True)


class incident_template(db.Model):
    """
    All data being storage on tables "incident_templates"

    id         | integer                        | not null
    
    name       | character varying(255)         | not null

    slug       | character varying(255)         | not null

    template   | text                           | not null

    created_at | timestamp(0) without time zone | 

    updated_at | timestamp(0) without time zone | 

    deleted_at | timestamp(0) without time zone | 
    """

    __tablename__ = "incident_templates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    template = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    deleted_at = db.Column(db.String(26))