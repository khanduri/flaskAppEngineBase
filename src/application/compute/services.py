from application.compute import models


def get_all_computes():
    computes = models.ComputeModel.query()
    return computes


def get_compute(compute_id):
    compute = models.ComputeModel.get_by_id(compute_id)
    return compute


def save_compute(a, b):
    compute = models.ComputeModel(a=a, b=b)
    return compute.put()


def delete_compute():
    pass
