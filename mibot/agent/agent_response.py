from flask import Blueprint, request, abort, jsonify
from flask_jwt_extended import jwt_required, current_user

from mibot.knowledge.models import Knowledge

from .serializer import ResponseRequest
from mibot.knowledge.serializer import KnowledgeResponse

from mibot.utils.chatbot import Chatbot

app = Blueprint('agent-reponse', __name__)


@app.route('', methods=['POST'])
# @jwt_required()
def create():
    data = ResponseRequest().load(request.get_json())

    try:
        knowledge = Knowledge.objects(agent=data['agent'])

        chatbot = Chatbot()
        chatbot.train(knowledge)
        res = chatbot.getResponse(data['message'])
    except:
        abort(401, 'No autorizado')

    return jsonify(res)
