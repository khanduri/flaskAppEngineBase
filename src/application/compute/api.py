import application.compute.services
import application.base.api


##########################################
# Collection operations
##########################################


def get_all_computes():
    computes = application.compute.services.fetch_all_computes()
    compute_list = [e.get_dict_repr() for e in computes]
    return application.base.api.get_json_packet(data=compute_list)


def update_all_computes():
    application.compute.services.modify_all_computes()


def post_compute():
    # TODO: read form here
    a, b = (14, 15)
    application.compute.services.create_new_compute(a, b)


def delete_all_computes():
    raise NotImplementedError()


##########################################
# Resource operations
##########################################


def get_compute(compute_id):
    compute_instance = application.compute.services.fetch_compute(compute_id)
    return application.base.api.get_json_packet(compute_instance.get_dict_repr())


def update_compute(compute_id):
    raise NotImplementedError()


def delete_compute(compute_id):
    raise NotImplementedError()

