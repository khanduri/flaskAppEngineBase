"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.
"""
from flask import render_template, url_for, redirect

from flask_cache import Cache

from application import app
from decorators import login_required, admin_required
from models import ExampleModel


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


def home():
    return redirect(url_for('computes_home'))


def warmup():
    """
    App Engine warmup handler
    See https://cloud.google.com/appengine/docs/python/config/appconfig?csw=1#Python_app_yaml_Warmup_requests
    """
    return ''


@login_required
def list_examples():
    examples = ExampleModel.query()
    return render_template('list_examples.html', examples=examples)


@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'


@cache.cached(timeout=60)
def cached_examples():
    """This view should be cached for 60 sec"""
    examples = ExampleModel.query()
    return render_template('list_examples_cached.html', examples=examples)


