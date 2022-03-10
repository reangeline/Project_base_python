from mongoengine import Document, StringField, ObjectIdField, EmailField

from pydantic import BaseModel

class User(Document):
    _id: ObjectIdField()
    name = StringField(max_length=200, required=True)
    email = EmailField(max_length=200, required=True)
    password = StringField(max_length=200, required=True)


class UserBase(BaseModel):
    id: str
    name: str
    email: str
    password: str

