import hashlib
import jwt
import application.core.settings


def encode_password(password):
    return hashlib.md5(password).hexdigest()


def encode_user_token(user):
    return jwt.encode({'user': user.to_json()}, application.core.settings.JWT_TOKEN_SECRET)
