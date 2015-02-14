import application.base.api
import application.compute.forms
import application.compute.services


##########################################
# Collection operations
##########################################


def get_all_computes():
    computes = application.compute.services.fetch_all_computes()
    compute_list = [e.get_dict_repr() for e in computes]
    return application.base.api.get_json_packet(data=compute_list)


def post_compute():
    form = application.compute.forms.ComputeForm(csrf_enabled=False)
    if form.validate_on_submit():
        application.compute.services.create_new_compute(form.data.get('a'), form.data.get('b'))
        return application.base.api.get_json_packet()
    return application.base.api.get_json_packet(status=404)


def delete_all_computes():
    application.compute.services.remove_all_computes()
    return application.base.api.get_json_packet()


##########################################
# Resource operations
##########################################


def get_compute(compute_id):
    compute_instance = application.compute.services.fetch_compute(compute_id)
    return application.base.api.get_json_packet(data=compute_instance.get_dict_repr())


def update_compute(compute_id):
    form = application.compute.forms.ComputeForm(csrf_enabled=False)
    if form.validate_on_submit():
        compute_instance = application.compute.services.modify_compute(compute_id, form.data.get('a'), form.data.get('b'))
        return application.base.api.get_json_packet(data=compute_instance.get_dict_repr())
    return application.base.api.get_json_packet(status=404)


def delete_compute(compute_id):
    application.compute.services.remove_compute(compute_id)
    return application.base.api.get_json_packet()

