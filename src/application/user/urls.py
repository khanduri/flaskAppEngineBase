import application
import application.user.api
import application.user.views
import application.user.tasks
import application.user.cron
import application.user.authentication


##########################################################################################
# Views
##########################################################################################
application.app.add_url_rule('/login', view_func=application.user.views.login, methods=['POST', 'GET'])
application.app.add_url_rule('/register', view_func=application.user.views.register, methods=['POST'])
application.app.add_url_rule('/verify', view_func=application.user.views.verify, methods=['GET'])
application.app.add_url_rule('/logout', view_func=application.user.views.logout, methods=['GET'])

application.app.add_url_rule('/login/<provider_name>/', view_func=application.user.authentication.social_login, methods=['GET', 'POST'])

##########################################################################################
# API
##########################################################################################
application.app.add_url_rule('/api/users', view_func=application.user.api.get_all_users, methods=['GET'])
application.app.add_url_rule('/api/users', view_func=application.user.api.post_user, methods=['POST'])

application.app.add_url_rule('/api/users/<int:user_id>', view_func=application.user.api.get_user, methods=['GET'])
application.app.add_url_rule('/api/users/<int:user_id>', view_func=application.user.api.update_user, methods=['PUT'])


##########################################################################################
# Tasks
##########################################################################################
# application.app.add_url_rule('/tasks/users', view_func=application.user.tasks.users, methods=['GET'])
# application.app.add_url_rule('/procs/users', view_func=application.user.tasks.users_procs, methods=['POST'])


##########################################################################################
# Cron
##########################################################################################
# application.app.add_url_rule('/cron/users/cleanup', view_func=application.user.cron.cleanup, methods=['GET'])
