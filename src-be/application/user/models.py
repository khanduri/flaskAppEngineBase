import application.user.data.google_data_store


class UserModel(object):
    _public_attr = ['first', 'last', 'email', 'verified']

    def __init__(self, data):
        self.data = data
        for k, v in self.data.iteritems():
            setattr(self, k, v)

    def __repr__(self):
        return "; ".join(['%s - %s' % (k, v) for k, v in self.data.iteritems() if k in self._public_attr])

    def to_json(self):
        json_rep = {}
        for k, v in self.data.iteritems():
            if k in self._public_attr:
                json_rep.update({k: v})
        return json_rep


UserQuery = application.user.data.google_data_store.UserQuery(UserModel)
