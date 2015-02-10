from application.compute import services


def compute_desc():
    return "basic"


def compute(a, b):
    services.save_compute(a, b)
    return "a: %s + b: %s = %s" % (a, b, (a + b))


def fetch_computes():
    computes = services.get_all_computes()
    return "<BR />".join(["id:%s = a=%s + b=%s = %s" % (e.key.id(), e.a, e.b, e.a + e.b) for e in computes])