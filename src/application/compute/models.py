import application.compute.data.gae


class ComputeModel(object):

    def __init__(self, data):
        self.data = data
        for k, v in data.iteritems():
            setattr(self, k, v)


ComputeQuery = application.compute.data.gae.ComputeQuery(ComputeModel)
