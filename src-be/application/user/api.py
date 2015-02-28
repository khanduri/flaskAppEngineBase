import application.base.decorators
import application.user.forms
import application.user.services
import hashlib
import jwt


##########################################
# Collection operations
##########################################

@application.base.decorators.return_json
def get_all_users():
    users = application.user.services.fetch_all_users()
    user_list = [e.data for e in users]
    return 200, user_list


@application.base.decorators.return_json
def post_user():
    form = application.user.forms.UserForm(csrf_enabled=False)
    if form.validate_on_submit():
        email = form.data.get('email')

        user = application.user.services.fetch_by_email(email)
        if user:
            return 400, {}

        first = form.data.get('first')
        last = form.data.get('last')

        password = form.data.get('password')
        passhash = hashlib.md5(password).hexdigest()

        user = application.user.services.create_new_user(first, last, email, passhash)
        return 201, {'user_id': user.id}

    return 404, {}


##########################################
# Resource operations
##########################################


@application.base.decorators.return_json
def get_user(user_id):
    user_instance = application.user.services.fetch_user(user_id)
    return 200, user_instance.data


@application.base.decorators.return_json
def update_user(user_id):
    form = application.user.forms.UserForm(csrf_enabled=False)
    if form.validate_on_submit():
        email = form.data.get('email')

        user = application.user.services.fetch_by_email(email)
        if user:
            return 400, {}

        first = form.data.get('first')
        last = form.data.get('last')

        user_instance = application.user.services.modify_user(user_id)
        return 200, user_instance.data
    return 404, {}
