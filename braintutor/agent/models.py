from mongoengine import Document, ReferenceField, StringField

from braintutor.auth.route import User

class Agent(Document):
    created_by = ReferenceField(User, required=True)
    name = StringField(required=True)