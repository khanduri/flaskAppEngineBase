import flask
import time


def get_json_packet(ststus=200, data={}):
    return_dict = {
        'meta': {
            'status': 200,
            'time': int(time.time())
        },
        'data': data,
    }
    return flask.jsonify(**return_dict)
