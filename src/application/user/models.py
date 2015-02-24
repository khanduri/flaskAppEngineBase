import application.user.data.google_data_store


class UserModel(object):

    def __init__(self, data):
        self.data = data
        for k, v in data.iteritems():
            setattr(self, k, v)


UserQuery = application.user.data.google_data_store.UserQuery(UserModel)
