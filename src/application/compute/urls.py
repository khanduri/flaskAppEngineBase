import application
import application.compute.api
import application.compute.views


application.app.add_url_rule('/compute', view_func=application.compute.views.compute_desc, methods=['GET'])
application.app.add_url_rule('/compute/<int:a>/<int:b>', view_func=application.compute.views.compute, methods=['GET'])

application.app.add_url_rule('/api/computes', view_func=application.compute.api.fetch_computes, methods=['GET'])
application.app.add_url_rule('/api/computes', view_func=application.compute.api.replace_computes, methods=['PUT'])
application.app.add_url_rule('/api/computes', view_func=application.compute.api.create_compute, methods=['POST'])
application.app.add_url_rule('/api/computes', view_func=application.compute.api.remove_computes, methods=['DELETE'])
application.app.add_url_rule('/api/computes/<int:compute_id>', view_func=application.compute.api.fetch_compute, methods=['GET'])
application.app.add_url_rule('/api/computes/<int:compute_id>', view_func=application.compute.api.replace_compute, methods=['PUT'])
# application.app.add_url_rule('/api/computes/<int:compute_id>', view_func=, methods=['POST'])  # NOT GENERALLY USED
application.app.add_url_rule('/api/computes/<int:compute_id>', view_func=application.compute.api.remove_compute, methods=['DELETE'])
