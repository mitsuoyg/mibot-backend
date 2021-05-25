from mibot.user.models import User


def jwt_identity(header, payload):
    return User.objects(id=payload.get("sub").get('user_id')).first()


def identity_loader(user):
    return user
