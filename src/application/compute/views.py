import application


##########################################
# GET RID OF THE FOLLOWING
##########################################


def compute_desc():
    return "basic"


def compute(a, b):
    application.compute.services.save_compute(a, b)
    return "a: %s + b: %s = %s" % (a, b, (a + b))
