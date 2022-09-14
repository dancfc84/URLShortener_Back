from app import db
from models.base import BaseModel


class LinkModel(db.Model, BaseModel):

    __tablename__ = "links"

    full = db.Column(db.Text, nullable=False, unique=True)
    short = db.Column(db.Integer, unique=True)
    clicks = db.Column(db.Integer,nullable=False,default=0)
