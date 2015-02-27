import application.user.data.google_data_store


class UserModel(object):

    def __init__(self, data):
        self.data = data
        for k, v in self.data.iteritems():
            setattr(self, k, v)

    def __repr__(self):
        repr_list = ['verified']
        return "; ".join(['%s - %s' % (k, v) for k, v in self.data.iteritems() if k in repr_list])


UserQuery = application.user.data.google_data_store.UserQuery(UserModel)
