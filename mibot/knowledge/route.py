from flask import Blueprint, request, abort, jsonify
from flask_jwt_extended import jwt_required, current_user
from bson.json_util import dumps

from .models import Agent
from .models import Knowledge, assert_can_edit

from .serializer import KnowledgeResponse, KnowledgeRequest

app = Blueprint('knowledge', __name__)


@app.route('', methods=['GET'])
@jwt_required()
def index():
    agent = request.args.get('agent')

    try:
        Agent.objects(id=agent, created_by=current_user.id).get()
    except:
        abort(401, 'No autorizado')

    knowledge = Knowledge.objects(agent=agent)

    return jsonify(KnowledgeResponse(many=True).dump(knowledge))


@app.route('<id>', methods=['GET'])
@jwt_required()
def show(id):
    try:
        knowledge = Knowledge.objects(id=id).get()
        assert_can_edit(current_user, knowledge)
    except:
        abort(401, 'No autorizado')

    return jsonify(KnowledgeResponse().dump(knowledge))


@app.route('', methods=['POST'])
@jwt_required()
def create():
    data = KnowledgeRequest().load(request.get_json())

    try:
        Agent.objects(id=data['agent'], created_by=current_user.id).get()
    except:
        abort(401, 'No autorizado')

    try:
        knowledge = Knowledge(**data).save()
    except:
        abort(422, 'Datos incorrectos')

    return dumps({'id': str(knowledge.id)}, ensure_ascii=False)


@app.route('<id>', methods=['PATCH'])
@jwt_required()
def update(id):
    data = KnowledgeRequest().load(request.get_json())

    try:
        knowledge = Knowledge.objects(id=id).get()
        assert_can_edit(current_user, knowledge)
    except:
        abort(401, 'No autorizado')

    try:
        knowledge.update(questions=data['questions'], answers=data['answers'])
    except:
        abort(422, 'Datos incorrectos')

    return jsonify(message="Ok")


@app.route('<id>', methods=['DELETE'])
@jwt_required()
def destroy(id):
    try:
        knowledge = Knowledge.objects(id=id).get()
        assert_can_edit(current_user, knowledge)
        knowledge.delete()
    except:
        abort(401, 'No autorizado')

    return jsonify(message="Ok")
