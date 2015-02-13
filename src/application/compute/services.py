from application.compute import models


def fetch_all_computes():
    computes = models.ComputeModel.query()
    return computes


def create_new_compute(a, b):
    compute = models.ComputeModel(a=a, b=b)
    return compute.put()


def modify_all_computes():
    raise NotImplementedError()


def remove_all_computes():
    raise NotImplementedError()


def fetch_compute(compute_id):
    compute = models.ComputeModel.get_by_id(compute_id)
    return compute


def modify_compute(compute_id):
    raise NotImplementedError()


def remove_compute(compute_id):
    raise NotImplementedError()
