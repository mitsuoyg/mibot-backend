from flask import Blueprint, request, abort
from flask_jwt_extended import create_access_token, jwt_required, current_user
from braintutor.extensions import bcrypt
from bson.json_util import dumps

from braintutor.user.models import User

app = Blueprint('auth', __name__)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    try:
        user = User.objects(username=username).get()
    except:
        abort(401, 'Usuario no existe')
    if not bcrypt.check_password_hash(user.password, password):
        abort(401, 'Contraseña incorrecta')

    token = create_access_token(identity={'user_id': str(user.id)})

    return dumps({'token': token}, ensure_ascii=False)


@app.route('/user', methods=['GET'])
@jwt_required()
def user():
    user = current_user.to_mongo().to_dict()

    return dumps({'user': user}, ensure_ascii=False)
