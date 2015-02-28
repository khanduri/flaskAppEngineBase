import google.appengine.api.taskqueue
import requests
import flask
import application.user.services


def users():
    google.appengine.api.taskqueue.add(url='/procs/users', params={})
    return 'Proc Queued!'


def users_procs():
    return 'Proc Done!'
