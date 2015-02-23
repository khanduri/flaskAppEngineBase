#!/usr/bin/env python
# encoding: utf-8
"""
generate_keys.py

Generate CSRF and Session keys, output to secret_keys.py file

Usage:
    generate_keys.py [-f]

Outputs secret_keys.py file in current folder

By default, an existing secret_keys file will not be replaced.
Use the '-f' flag to force the new keys to be written to the file


"""

import string
import os.path
import optparse
import random


# File settings
file_name = 'secret_keys.py'
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)

file_template = string.Template('''
#############################################
# CSRF- and Session keys
#############################################
CSRF_SECRET_KEY = '$csrf_key'
SESSION_KEY = '$session_key'


#############################################
# Base Settings
#############################################
SESSION_EXPIRATION = 90 * 24 * 60 * 60  # days * hours * minutes * seconds


#############################################
# EMail Settings
#############################################
class Emails(object):
    NO_REPLY = ''
    SITE_ADMIN = ''


#############################################
# Sendgrid settings (your sendgrid username and password here)
#############################################
SENDGRID_USERNAME = ''
SENDGRID_PASSWORD = ''


#############################################
# Authomatic
#############################################
AUTHOMATIC_SECRET_STRING = '$authomatic_key'

FB_APP_ID = ''
FB_APP_SECRET = ''

TW_CONSUMER_KEY = ''
TW_CONSUMER_SECRET = ''
''')


# Get options from command line
parser = optparse.OptionParser()
parser.add_option(
    "-f", "--force", dest="force",
    help="force overwrite of existing secret_keys file", action="store_true")
parser.add_option(
    "-r", "--randomness", dest="randomness",
    help="length (randomness) of generated key; default = 24", default=24)
(options, args) = parser.parse_args()


def generate_randomkey(length):
    """Generate random key, given a number of characters"""
    chars = string.letters + string.digits
    return ''.join([random.choice(chars) for _ in range(length)])


def write_file(contents):
    with open(file_path, 'wb') as f:
        f.write(contents)


def generate_keyfile():

    r = options.randomness
    csrf_key = generate_randomkey(r)
    session_key = generate_randomkey(r)
    authomatic_key = generate_randomkey(r)

    output = file_template.safe_substitute(dict(
        csrf_key=csrf_key,
        session_key=session_key,
        authomatic_key=authomatic_key,
    ))

    if options.force is not None:
        write_file(output)
        return

    if not os.path.exists(file_path):
        write_file(output)
        return

    print "Warning: secret_keys.py file exists.  Use 'generate_keys.py --force' to force overwrite."



if __name__ == "__main__":
    generate_keyfile()
