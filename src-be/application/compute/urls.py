import application
import application.compute.api
import application.compute.views
import application.compute.tasks
import application.compute.cron


##########################################################################################
# Views
##########################################################################################

application.app.add_url_rule('/computes', 'computes_home', view_func=application.compute.views.compute_desc, methods=['GET'])
application.app.add_url_rule('/compute/<int:a>/<int:b>', view_func=application.compute.views.compute, methods=['GET'])

##########################################################################################
# API
##########################################################################################

application.app.add_url_rule('/api/computes', view_func=application.compute.api.get_all_computes, methods=['GET'])
# application.app.add_url_rule('/api/computes', view_func=, methods=['PUT'])  # IGNORING IT FOR NOW
application.app.add_url_rule('/api/computes', view_func=application.compute.api.post_compute, methods=['POST'])
application.app.add_url_rule('/api/computes', view_func=application.compute.api.delete_all_computes, methods=['DELETE'])

application.app.add_url_rule('/api/computes/<int:compute_id>', view_func=application.compute.api.get_compute, methods=['GET'])
application.app.add_url_rule('/api/computes/<int:compute_id>', view_func=application.compute.api.update_compute, methods=['PUT'])
# application.app.add_url_rule('/api/computes/<int:compute_id>', view_func=, methods=['POST'])  # NOT GENERALLY USED
application.app.add_url_rule('/api/computes/<int:compute_id>', view_func=application.compute.api.delete_compute, methods=['DELETE'])

##########################################################################################
# Tasks
##########################################################################################

application.app.add_url_rule('/tasks/computes', view_func=application.compute.tasks.computes, methods=['GET'])
application.app.add_url_rule('/procs/computes', view_func=application.compute.tasks.computes_procs, methods=['POST'])

##########################################################################################
# Cron
##########################################################################################

application.app.add_url_rule('/cron/computes/cleanup', view_func=application.compute.cron.cleanup, methods=['GET'])
