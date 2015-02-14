import google.appengine.ext.ndb
import application.base.models


class ComputeModel(application.base.models.DictableModel):

    a = google.appengine.ext.ndb.IntegerProperty(required=True)
    b = google.appengine.ext.ndb.IntegerProperty(required=True)

    def get_dict_repr(self):
        data = super(ComputeModel, self).get_dict_repr()
        data.update({
            'a': self.a,
            'b': self.b,
        })
        return data
