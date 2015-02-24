import application.user.models


##########################################
# Collection operations
##########################################


def fetch_all_users():
    users = application.user.models.UserQuery.select_all()
    return users


def create_new_user(first, last, email, passhash):
    user = application.user.models.UserQuery.insert_single(first, last, email, passhash)
    # TODO: send verification email here
    return user


##########################################
# Resource operations
##########################################


def fetch_user(user_id):
    user = application.user.models.UserQuery.select_by_id(user_id)
    return user


def modify_user(user_id, first=None, last=None, passhash=None):
    user = application.user.models.UserQuery.update_by_id(user_id, first=first, last=last, passhash=passhash)
    return user


def fetch_by_email(email):
    if not email:
        return None

    user = application.user.models.UserQuery.select_by_email(email)
    return user


def modify_user_validity(user_id, verified):
    user = application.user.models.UserQuery.update_by_id(user_id, verified=verified)
    return user


def fetch_by_login(email, passhash):
    user = application.user.models.UserQuery.select_by_login(email, passhash)
    return user
