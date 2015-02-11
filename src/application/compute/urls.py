from application import app
from application.compute import api


app.add_url_rule('/compute', view_func=api.compute_desc, methods=['GET'])
app.add_url_rule('/compute/<int:a>/<int:b>', view_func=api.compute, methods=['GET'])

app.add_url_rule('/computes', view_func=api.fetch_computes, methods=['GET'])
