import time
import application.user.services
import random


def cleanup():
    curren_time = int(time.time())

    users = application.user.services.fetch_all_users()
    user = random.choice(users)
    # application.user.services.remove_user(user.id)

    return 'Done!'