from marshmallow import Schema, fields


class AgentResponse(Schema):
    id = fields.Str()
    name = fields.Str()

class ResponseRequest(Schema):
    agent = fields.Str()
    message = fields.Str()
