import authomatic.providers.oauth1
import authomatic.providers.oauth2
import application.secret_keys


SESSION_EXPIRATION = application.secret_keys.SESSION_EXPIRATION
JWT_TOKEN_SECRET =  application.secret_keys.JWT_TOKEN_SECRET


#############################################
# Emails
#############################################
class EMails(object):
    NO_REPLY = application.secret_keys.Emails.NO_REPLY
    SITE_ADMIN = application.secret_keys.Emails.SITE_ADMIN


#############################################
# Sendgrid settings (your sendgrid username and password here)
#############################################
SENDGRID_USERNAME = application.secret_keys.SENDGRID_USERNAME
SENDGRID_PASSWORD = application.secret_keys.SENDGRID_PASSWORD


#############################################
# Authomatic
#############################################
AUTHOMATIC_SECRET_STRING = application.secret_keys.AUTHOMATIC_SECRET_STRING

AUTHOMATIC_CONFIG = {
    'tw': {
        # make sure to make the edit to /etc/hosts
        'class_': authomatic.providers.oauth1.Twitter,
        'consumer_key': application.secret_keys.TW_CONSUMER_KEY,
        'consumer_secret': application.secret_keys.TW_CONSUMER_SECRET,
    },
    'fb': {
        'class_': authomatic.providers.oauth2.Facebook,
        'consumer_key': application.secret_keys.FB_APP_ID,
        'consumer_secret': application.secret_keys.FB_APP_SECRET,
        'scope': ['user_about_me', 'email', 'publish_stream'],
    },
}


#############################################
# Basic Config
#############################################
class Config(object):
    # Set secret keys for CSRF protection
    SECRET_KEY = application.secret_keys.CSRF_SECRET_KEY
    CSRF_SESSION_KEY = application.secret_keys.SESSION_KEY
    # Flask-Cache settings
    CACHE_TYPE = 'gaememcached'


class Development(Config):
    DEBUG = True
    # Flask-DebugToolbar settings
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CSRF_ENABLED = True


class Testing(Config):
    TESTING = True
    DEBUG = True
    CSRF_ENABLED = True


class Production(Config):
    DEBUG = False
    CSRF_ENABLED = True