import flask
import flask_cache
import application

# Flask-Cache (configured to use App Engine Memcache API)
cache = flask_cache.Cache(application.app)


def home():
    return flask.redirect('/login')


def warmup():
    """
    App Engine warmup handler
    See https://cloud.google.com/appengine/docs/python/config/appconfig?csw=1#Python_app_yaml_Warmup_requests
    """
    return ''

