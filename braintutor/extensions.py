from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from braintutor.utils.auth import jwt_identity, identity_loader

from braintutor.integrations.storage import FlaskFirebase

jwt = JWTManager()
jwt.user_lookup_loader(jwt_identity)
jwt.user_identity_loader(identity_loader)

bcrypt = Bcrypt()
cors = CORS()
db = MongoEngine()
storage = FlaskFirebase()
