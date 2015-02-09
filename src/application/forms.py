"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flask_wtf import Form
from wtforms import fields
from wtforms import validators
from wtforms.ext.appengine.ndb import model_form

from .models import ExampleModel


class ClassicExampleForm(Form):
    example_name = fields.StringField('Name', validators=[validators.Required()])
    example_description = fields.TextAreaField('Description', validators=[validators.Required()])

# App Engine ndb model form example
ExampleForm = model_form(ExampleModel, Form, field_args={
    'example_name': dict(validators=[validators.Required()]),
    'example_description': dict(validators=[validators.Required()]),
})
