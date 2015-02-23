import flask
import flask_cache
import application.core.decorators


# Flask-Cache (configured to use App Engine Memcache API)
cache = flask_cache.Cache(application.app)


def home():
    return flask.render_template('index.html', result=None)


def warmup():
    """
    App Engine warmup handler
    See https://cloud.google.com/appengine/docs/python/config/appconfig?csw=1#Python_app_yaml_Warmup_requests
    """
    return ''


############## REMOVE THIS #################
@application.core.decorators.admin_required
def admin_only():
    return 'Super-seekrit admin page.'

@cache.cached(timeout=60)
def cached_examples():
    examples = None
    return flask.render_template('list_examples_cached.html', examples=examples)
############## REMOVE THIS #################