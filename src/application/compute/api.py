from application.compute import services
from application.base import api as base_api


def compute_desc():
    return "basic"


def compute(a, b):
    services.save_compute(a, b)
    return "a: %s + b: %s = %s" % (a, b, (a + b))


def fetch_computes():
    computes = services.get_all_computes()
    compute_list = [{'id': e.key.id(), 'a': e.a, 'b': e.b, 'compute': e.a + e.b} for e in computes]
    return base_api.get_json_packet(compute_list)

