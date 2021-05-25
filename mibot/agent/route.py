from flask import Blueprint, abort, jsonify
from flask_jwt_extended import jwt_required, current_user

from .models import Agent

from .serializer import AgentResponse

app = Blueprint('agent', __name__)


@app.route('', methods=['GET'])
@jwt_required()
def index():
    user = current_user

    agents = Agent.objects(created_by=user.id)

    return jsonify(AgentResponse(many=True).dump(agents))


@app.route('<id>', methods=['GET'])
@jwt_required()
def show(id):
    user = current_user

    try:
        agent = Agent.objects(id=id, created_by=user.id).get()
    except:
        abort(401, 'No autorizado')

    return jsonify(AgentResponse().dump(agent))
