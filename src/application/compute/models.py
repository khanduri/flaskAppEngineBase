from google.appengine.ext import ndb
from application.base.models import BaseModel


class ComputeModel(BaseModel):
    example_name = ndb.StringProperty(required=True)
    example_description = ndb.TextProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
