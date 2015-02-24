import flask

import application.core.views



## URL dispatch rules
# App Engine warm up handler
# See https://cloud.google.com/appengine/docs/python/config/appconfig?csw=1#Python_app_yaml_Warmup_requests
application.app.add_url_rule('/_ah/warmup', 'warmup', view_func=application.core.views.warmup)

application.app.add_url_rule('/', 'home', view_func=application.core.views.home)

############## REMOVE THIS #################
application.app.add_url_rule('/examples/cached', 'cached_examples', view_func=application.core.views.cached_examples, methods=['GET'])
############## REMOVE THIS #################

import application.compute.urls
import application.user.urls


## Error handlers
# Handle 404 errors
@application.app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404

# Handle 500 errors
@application.app.errorhandler(500)
def server_error(e):
    return flask.render_template('500.html'), 500
