from google.appengine.ext import ndb


class BaseModel(ndb.Model):
    timestamp_created = ndb.DateTimeProperty(auto_now_add=True)
    timestamp_removed = ndb.DateTimeProperty(auto_now_add=True)
    timestamp_modified = ndb.DateTimeProperty(auto_now_add=True)
