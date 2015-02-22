import os

import flask
import flask_debugtoolbar
import werkzeug.debug



app = flask.Flask('application')


if os.getenv('FLASK_CONF') == 'TEST':
    app.config.from_object('application.core.settings.Testing')

elif 'SERVER_SOFTWARE' in os.environ and os.environ['SERVER_SOFTWARE'].startswith('Dev'):
    # Development settings
    app.config.from_object('application.core.settings.Development')
    # Flask-DebugToolbar
    toolbar = flask_debugtoolbar.DebugToolbarExtension(app)

    # Google app engine mini profiler
    # https://github.com/kamens/gae_mini_profiler
    app.wsgi_app = werkzeug.debug.DebuggedApplication(app.wsgi_app, evalex=True)

    # from gae_mini_profiler import profiler, templatetags
    # @app.context_processor
    # def inject_profiler():
        # return dict(profiler_includes=templatetags.profiler_includes())
    # app.wsgi_app = profiler.ProfilerWSGIMiddleware(app.wsgi_app)

else:
    app.config.from_object('application.core.settings.Production')

# Enable jinja2 loop controls extension
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# Pull in URL dispatch routes
from application.core import authentication, urls
