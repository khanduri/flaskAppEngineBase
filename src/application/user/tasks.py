import google.appengine.api.taskqueue
import requests
import flask
import application.user.services


def users():
    url1 = flask.request.values.get('url1')
    url2 = flask.request.values.get('url2')

    google.appengine.api.taskqueue.add(url='/procs/users', params={'url1': url1, 'url2': url2})

    return 'Proc Queued!'


def users_procs():
    url1 = flask.request.values.get('url1')
    temp1 = requests.get(url1)
    a = len(temp1.text.split(' '))

    url2 = flask.request.values.get('url2')
    temp2 = requests.get(url2)
    b = len(temp2.text.split(' '))

    application.user.services.create_new_user(None, None, None, None)

    return 'Done!'
