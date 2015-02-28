import time
import application.compute.services
import random


def cleanup():
    curren_time = int(time.time())

    computes = application.compute.services.fetch_all_computes()
    compute = random.choice(computes)
    application.compute.services.remove_compute(compute.id)

    return 'Done!'