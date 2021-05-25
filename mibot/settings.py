"""Application configuration."""

# TODO: read from env
import os


class Config(object):
    """Base configuration."""

    JWT_SECRET_KEY = 'mibot'
    JWT_AUTH_HEADER_PREFIX = 'Bearer'
    JWT_ACCESS_TOKEN_EXPIRES = 8 * 60 * 60

    UPLOAD_FOLDER = 'temp'
    MAX_CONTENT_LENGTH = 25 * 1024 * 1024


class TestingConfig(Config):
    # STORAGE_BUCKET = "mibot.appspot.com"
    DATABASE_NAME = "test"
    MONGODB_HOST = "mongomock://localhost"
    TESTING = True


class DevelopmentConfig(Config):
    # STORAGE_BUCKET = "mibot.appspot.com"
    DATABASE_NAME = "mibot-prod"
    MONGODB_HOST = os.environ.get(
        "MONGODB_HOST", "mongodb+srv://mitsuoyg:Yshara159@cluster.u1gxy.mongodb.net/mibot-prod?retryWrites=true&w=majority")


class ProductionConfig(Config):
    # STORAGE_BUCKET = "mibot.appspot.com"
    DATABASE_NAME = "mibot-prod"
    MONGODB_HOST = "mongodb+srv://mitsuoyg:Yshara159@cluster.u1gxy.mongodb.net/mibot-prod?retryWrites=true&w=majority"


envs = {
    'production': ProductionConfig(),
    'development': DevelopmentConfig()
}


def getConfig():
    return envs[os.environ.get('FLASK_ENV', 'production')]
