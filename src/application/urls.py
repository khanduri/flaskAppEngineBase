"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

import application
import application.views


## URL dispatch rules
# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
application.app.add_url_rule('/_ah/warmup', 'warmup', view_func=application.views.warmup)

# Home page
application.app.add_url_rule('/', 'home', view_func=application.views.home)

# Say hello
application.app.add_url_rule('/hello/<username>', 'say_hello', view_func=application.views.say_hello)

# Examples list page
application.app.add_url_rule('/examples', 'list_examples', view_func=application.views.list_examples, methods=['GET', 'POST'])

# Examples list page (cached)
application.app.add_url_rule('/examples/cached', 'cached_examples', view_func=application.views.cached_examples, methods=['GET'])

# Contrived admin-only view example
application.app.add_url_rule('/admin_only', 'admin_only', view_func=application.views.admin_only)

# Edit an example
application.app.add_url_rule('/examples/<int:example_id>/edit', 'edit_example', view_func=application.views.edit_example, methods=['GET', 'POST'])

# Delete an example
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

