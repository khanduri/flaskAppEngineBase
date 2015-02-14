import application.compute.models


##########################################
# Collection operations
##########################################


def fetch_all_computes():
    computes = application.compute.models.ComputeModel.query()
    return computes


def create_new_compute(a, b):
    compute = application.compute.models.ComputeModel(a=a, b=b)
    return compute.put()


def remove_all_computes():
    computes = application.compute.models.ComputeModel.query()
    list_of_keys = [c.key for c in computes]
    import google.appengine.ext.ndb
    google.appengine.ext.ndb.delete_multi(list_of_keys)


##########################################
# Resource operations
##########################################


def fetch_compute(compute_id):
    compute = application.compute.models.ComputeModel.get_by_id(compute_id)
    return compute


def modify_compute(compute_id, a, b):
    compute = application.compute.models.ComputeModel.get_by_id(compute_id)
    compute.a = a
    compute.b = b
    compute.put()
    return compute


def remove_compute(compute_id):
    compute = application.compute.models.ComputeModel.get_by_id(compute_id)
    compute.key.delete()
    return True
