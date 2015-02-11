import application.compute.services
import application.base.api


##########################################
# Collection operations
##########################################


def fetch_computes():
    computes = application.compute.services.get_all_computes()
    compute_list = [e.get_dict_repr() for e in computes]
    return application.base.api.get_json_packet(compute_list)


def replace_computes():
    raise NotImplementedError()


def create_compute():
    raise NotImplementedError()


def remove_computes():
    raise NotImplementedError()


##########################################
# Resource operations
##########################################


def fetch_compute(compute_id):
    compute_instance = application.compute.services.get_compute(compute_id)
    return application.base.api.get_json_packet(compute_instance.get_dict_repr())


def replace_compute(compute_id):
    raise NotImplementedError()


def remove_compute(compute_id):
    raise NotImplementedError()


##########################################
# GET RID OF THE FOLLOWING
##########################################


def compute_desc():
    return "basic"


def compute(a, b):
    application.compute.services.save_compute(a, b)
    return "a: %s + b: %s = %s" % (a, b, (a + b))

