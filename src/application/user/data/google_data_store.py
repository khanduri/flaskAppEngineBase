import google.appengine.ext.ndb
import uuid


class User(google.appengine.ext.ndb.Model):
    email = google.appengine.ext.ndb.StringProperty()
    first = google.appengine.ext.ndb.StringProperty()
    last = google.appengine.ext.ndb.StringProperty()
    passhash = google.appengine.ext.ndb.StringProperty()
    verified = google.appengine.ext.ndb.BooleanProperty()
    verification_code = google.appengine.ext.ndb.StringProperty()

    timestamp_created = google.appengine.ext.ndb.DateTimeProperty(auto_now=True)
    timestamp_removed = google.appengine.ext.ndb.DateTimeProperty(auto_now=True)
    timestamp_modified = google.appengine.ext.ndb.DateTimeProperty(auto_now=True)

    def get_dict_repr(self):
        data = {
            'id': self.key.id(),

            'email': self.email,
            'first': self.first,
            'last': self.last,
            'verification_code': self.verification_code,
            'verified': self.verified,

            'timestamp_created': self.timestamp_created,
            'timestamp_removed': self.timestamp_removed,
            'timestamp_modified': self.timestamp_modified,
        }
        return data


class UserQuery(object):

    def __init__(self, model_class):
        self.model_class = model_class

    ##########################################
    # Collection operations
    ##########################################

    def select_all(self):
        users = User.query().order(-User.timestamp_created)
        return [self.model_class(c.get_dict_repr()) for c in users]

    def insert_single(self, first, last, email, passhash):
        user = User(first=first, last=last, email=email, passhash=passhash)
        user.verified = False
        user.verification_code = uuid.uuid4().hex
        user.put()
        return self.model_class(user.get_dict_repr())

    ##########################################
    # Resource operations
    ##########################################

    def select_by_id(self, user_id):
        user = User.get_by_id(user_id)
        return self.model_class(user.get_dict_repr())

    def select_by_login(self, email, passhash):
        users = User.query(User.email == email, User.passhash == passhash).fetch()
        # todo: check for the len(users)
        user = users[0] if users else None
        return self.model_class(user.get_dict_repr()) if user else None

    def select_by_email(self, email):
        users = User.query(User.email == email).fetch()
        # todo: check for the len(users)
        user = users[0] if users else None
        return self.model_class(user.get_dict_repr()) if user else None

    def update_by_id(self, user_id, first=None, last=None, passhash=None, verified=None):
        user = User.get_by_id(user_id)

        if first is not None:
            user.first = first
        if last is not None:
            user.last = last
        if passhash is not None:
            user.passhash = passhash
        if verified is not None:
            user.verified = verified

        user.put()
        return self.model_class(user.get_dict_repr())
