"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

import application
import application.views


## URL dispatch rules
# App Engine warm up handler
# See https://cloud.google.com/appengine/docs/python/config/appconfig?csw=1#Python_app_yaml_Warmup_requests
application.app.add_url_rule('/_ah/warmup', 'warmup', view_func=application.views.warmup)

application.app.add_url_rule('/', 'home', view_func=application.views.home)
application.app.add_url_rule('/admin_only', 'admin_only', view_func=application.views.admin_only)
application.app.add_url_rule('/examples', 'list_examples', view_func=application.views.list_examples, methods=['GET', 'POST'])
application.app.add_url_rule('/examples/cached', 'cached_examples', view_func=application.views.cached_examples, methods=['GET'])
application.app.add_url_rule('/examples/<int:example_id>/edit', 'edit_example', view_func=application.views.edit_example, methods=['GET', 'POST'])
application.app.add_url_rule('/examples/<int:example_id>/delete', view_func=application.views.delete_example, methods=['POST'])


import application.compute.urls


## Error handlers
# Handle 404 errors
@application.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@application.app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

