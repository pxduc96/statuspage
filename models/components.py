"""
Using a define component and reference it
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')

class component(db.Model):
    """
    All data being storage on table "components"

    id          | integer                        | not null

    name        | character varying(255)         | not null

    description | text                           | not null

    link        | text                           | not null

    status      | integer                        | not null

    order       | integer                        | not null

    group_id    | integer                        | not null

    created_at  | timestamp(0) without time zone | 

    updated_at  | timestamp(0) without time zone | 

    deleted_at  | timestamp(0) without time zone | 

    enabled     | boolean                        | not null default true
    """

    __tablename__ = "components"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False, default="")
    link = db.Column(db.Text)
    status = db.Column(db.Integer, nullable=False, default=0, index=True)
    order = db.Column(db.Integer, nullable=False, default=0, index=True)
    group_id = db.Column(db.Integer, nullable=False, default=0, index=True)
    enabled = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    deleted_at = db.Column(db.String(26))

class component_group(db.Model):
    """
    All data being storage on table "component_groups"

    id         | integer                        | not null

    name       | character varying(255)         | not null

    created_at | timestamp(0) without time zone | 

    updated_at | timestamp(0) without time zone | 

    order      | integer                        | not null default 0

    collapsed  | integer                        | not null default 1
    """

    __tablename__ = "component_groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    order = db.Column(db.Integer, default=0, index=True)
    collapsed = db.Column(db.Integer, default=1)


class component_tag(db.Model):
    """
    All data being storage on table "component_tag"

    id           | integer | not null

    component_id | integer | not null
    
    tag_id       | integer | not null
    """

    __tablename__ = "component_tag"

    id = db.Column(db.Integer, primary_key=True)
    component_id = db.Column(db.Integer, nullable=False, index=True)
    tag_id = db.Column(db.Integer, nullable=False, index=True)
