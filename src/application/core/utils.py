import google.appengine.api.memcache
import application.core.settings
import datetime
import uuid
import hashlib


class Session(object):

    def remove(self):
        if self.sid:
            google.appengine.api.memcache.delete(self.sid)

    def set(self, email, ip):
        sid = hashlib.md5(uuid.uuid4().hex).hexdigest()
        exp = datetime.datetime.now() + datetime.timedelta(seconds=application.core.settings.SESSION_EXPIRATION)
        expires = exp.strftime("%a, %d %b %Y %H:%M:%S GMT")

        cache_data = {'email': email, 'ip': ip, 'expires': expires}
        google.appengine.api.memcache.add(sid, cache_data)

        return sid

    def __init__(self, sid):
        self.ip = self.sid = self.email = None
        self.valid = False

        if not sid:
            return

        session = google.appengine.api.memcache.get(sid)
        if session:
            self.ip = session['ip']
            self.sid = sid
            self.email = session['email']
            self.valid = True
