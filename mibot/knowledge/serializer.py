from marshmallow import Schema, EXCLUDE, fields


class AnswerBlock(Schema):
    type = fields.Str()
    value = fields.Str()


class KnowledgeResponse(Schema):
    id = fields.Str()
    questions = fields.List(fields.Str())
    answers = fields.List(fields.List(fields.Nested(AnswerBlock)))


class KnowledgeRequest(Schema):
    class Meta:
        unknown = EXCLUDE

    agent = fields.Str()
    questions = fields.List(fields.Str())
    answers = fields.List(fields.List(fields.Nested(AnswerBlock)))
