from google.appengine.ext import ndb
from application.base.models import BaseModel


class ComputeModel(BaseModel):
    a = ndb.IntegerProperty()
    b = ndb.IntegerProperty()
