import google.appengine.ext.ndb


class BaseModel(google.appengine.ext.ndb.Model):
    timestamp_created = google.appengine.ext.ndb.DateTimeProperty(auto_now=True)
    timestamp_removed = google.appengine.ext.ndb.DateTimeProperty(auto_now=True)
    timestamp_modified = google.appengine.ext.ndb.DateTimeProperty(auto_now=True)


class DictableModel(BaseModel):

    def get_dict_repr(self):
        data = {
            'id': self.key.id(),
            'timestamp_created': self.timestamp_created,
            'timestamp_removed': self.timestamp_removed,
            'timestamp_modified': self.timestamp_modified,
        }
        return data

