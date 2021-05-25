from mongoengine import Document, EmbeddedDocument, ReferenceField, ListField, StringField, EmbeddedDocumentField

from mibot.agent.route import Agent

from flask import abort

ANSWER_TYPES = ('text', 'image')


class AnswerBlock(EmbeddedDocument):
    type = StringField(choices=ANSWER_TYPES, required=True)
    value = StringField(min_length=1, required=True)


class Knowledge(Document):
    agent = ReferenceField(Agent, required=True)
    questions = ListField(StringField(min_length=1), required=True)
    answers = ListField(
        ListField(EmbeddedDocumentField(AnswerBlock)), required=True)


def assert_can_edit(user, knowledge):
    if not user.id == knowledge.agent.created_by.id:
        abort(401, 'No autorizado')
