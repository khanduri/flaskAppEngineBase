from google.appengine.ext import ndb
from application.base.models import BaseModel


class ComputeModel(BaseModel):
    a = ndb.IntegerProperty(required=True)
    b = ndb.IntegerProperty(required=True)
