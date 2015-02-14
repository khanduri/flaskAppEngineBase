from application.compute import models


##########################################
# Collection operations
##########################################


def fetch_all_computes():
    computes = models.ComputeModel.query()
    return computes


def create_new_compute(a, b):
    compute = models.ComputeModel(a=a, b=b)
    return compute.put()


def remove_all_computes():
    raise NotImplementedError()


##########################################
# Resource operations
##########################################


def fetch_compute(compute_id):
    compute = models.ComputeModel.get_by_id(compute_id)
    return compute


def modify_compute(compute_id, a, b):
    compute = models.ComputeModel.get_by_id(compute_id)
    compute.a = a
    compute.b = b
    compute.put()
    return compute


def remove_compute(compute_id):
    raise NotImplementedError()
