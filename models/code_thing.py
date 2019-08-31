from app import db, ma
from .base import BaseModel, BaseSchema



class CodeThing(db.Model, BaseModel):

    __tablename__ = 'code_things'

    type = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120))
    language = db.Column(db.String(50))
    example = db.Column(db.String(120))
    explanation = db.Column(db.Text)
    link = db.Column(db.String(120),)

class CodeThingsSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = CodeThing
