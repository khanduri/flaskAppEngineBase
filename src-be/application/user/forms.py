import flask_wtf
import wtforms


class UserEmailResetForm(flask_wtf.Form):
    email = wtforms.StringField(label='email', validators=[wtforms.validators.Email(), wtforms.validators.DataRequired()])


class UserPasswordResetForm(flask_wtf.Form):
    email = wtforms.StringField(label='email', validators=[wtforms.validators.Email(), wtforms.validators.DataRequired()])
    password = wtforms.StringField(label='password', validators=[wtforms.validators.DataRequired()])
    reset_code = wtforms.StringField(label='reset_code', validators=[wtforms.validators.DataRequired()])


class UserLoginForm(flask_wtf.Form):
    email = wtforms.StringField(label='email', validators=[wtforms.validators.Email(), wtforms.validators.DataRequired()])
    password = wtforms.StringField(label='password', validators=[wtforms.validators.DataRequired()])


class UserForm(UserLoginForm):
    first = wtforms.StringField(label='first', validators=[wtforms.validators.DataRequired()])
    last = wtforms.StringField(label='last', validators=[wtforms.validators.DataRequired()])
    email = wtforms.StringField(label='email', validators=[wtforms.validators.Email(), wtforms.validators.DataRequired()])
    password = wtforms.StringField(label='password', validators=[wtforms.validators.DataRequired()])
