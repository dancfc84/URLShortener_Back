from app import ma
from models.links import LinkModel

class LinkSchema(ma.SQLAlchemyAutoSchema):

  class Meta:
    model = LinkModel
    load_instance = True