from flask import Flask
from mibot.settings import Config
from mibot.extensions import jwt, bcrypt, cors, db, storage
from mibot.errors import generic_error

from mibot.auth.route import app as auth
from mibot.agent.route import app as agent
from mibot.agent.agent_response import app as agent_response
from mibot.knowledge.route import app as knowledge


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errors(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
    db.init_app(app)
    # storage.init_app(app)


def register_blueprints(app):
    app.register_blueprint(auth, url_prefix='/api/auth')
    app.register_blueprint(agent, url_prefix='/api/agent')
    app.register_blueprint(agent_response, url_prefix='/api/agent-response')
    app.register_blueprint(knowledge, url_prefix='/api/knowledge')


def register_errors(app):
    app.register_error_handler(401, generic_error)
    app.register_error_handler(422, generic_error)
