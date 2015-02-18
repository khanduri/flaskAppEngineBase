# -*- coding: utf-8 -*-
import datetime

from selenium import webdriver

import constants

# Choose and configure the browser of your choice
def get_browser():
    return webdriver.Chrome()

# The host and port where the tested ap shoud listen.
HOST = '127.0.0.1'
PORT = 8080

# The host alias set in the /etc/hosts file.
# The actual tests will navigate selenium browser to this host.
# This is necessary because some providers don't support localhost as the
# callback url.
HOST_ALIAS = 'authomatic.com'

# Only providers included here will be tested.
# This is a convenience to easily exclude providers from tests by commenting
# them out.
INCLUDE_PROVIDERS = [
    'amazon',
    'bitly', # 5
    'deviantart',
    'eventbrite', # 4
    'facebook',
    'foursquare', # 1
    'google',
    'github', # 3
    'linkedin',
    'paypal',
    'reddit', # 2
    'vk',
    'windowslive',
    'yammer',
    'yandex',
]


# Use these constants if you have the same user info by all tested providers.
PASSWORD = '1Kokotina'
EMAIL = 'peterhudec@peterhudec.com'
FIRST_NAME = 'Peter'
LAST_NAME = 'Hudec'
NAME = FIRST_NAME + ' ' + LAST_NAME
USERNAME = 'peterhudec'
USERNAME_REVERSE = 'hudecpeter'
NICKNAME = 'hudo'
BIRTH_YEAR = '1979'
# TODO: Remove the coercion to str.
BIRTH_DATE = str(datetime.datetime(1979, 11, 18))
CITY = 'Bratislava'
COUNTRY = 'Slovakia'
POSTAL_CODE = '82107'
PHONE = '0903972845'
PHONE_INTERNATIONAL = '00421903972845'
GENDER = constants.GENDER_MALE
LOCALE = 'en_US'

# Common values for all providers
COMMON = {
    # Could be same if the user sets it so
    'user_birth_date': BIRTH_DATE,
    'user_login': EMAIL,
    'user_password': PASSWORD,
    'user_email': EMAIL,
    'user_first_name': FIRST_NAME,
    'user_last_name': LAST_NAME,
    'user_name': NAME,
    'user_username': USERNAME,
    'user_username_reverse': USERNAME_REVERSE,
    'user_nickname': NICKNAME,
    'user_birth_year': BIRTH_YEAR,
    'user_city': CITY,
    'user_country': COUNTRY,
    'user_gender': GENDER,
    'user_phone': PHONE,
    'user_postal_code': POSTAL_CODE,
    'user_locale': LOCALE,

    # Provider and user specific value
    # 'user_id': '',
    # 'user_locale': None,
    # 'user_timezone': None,

    # Provider specific format
    # 'user_picture': '',
    # 'user_link': '',

    # Provider specific value
    # 'consumer_key': '',
    # 'consumer_secret': '',
}

# Values from COMMON will be overriden by values from PROVIDERS[provider_name]
# if set.
PROVIDERS = {
    'amazon': {
        'consumer_key': 'amzn1.application-oa2-client.aac94a29737c4d86a734e5964696d2bd',
        'consumer_secret': 'bb1aa3772cd755d009ba419211fccde1e785021e1bbea4334235ca298dac42b0',
        'user_id': 'amzn1.account.AFQXBE5AJMX73ZABIBYD25ET2MZQ',
        'user_password': 'Ebencikrista4krat',
    },
    'behance': {
        'consumer_key': 'J6MwhGHdTHwwYQEHyTq2jNgly0EEXixe',
        'consumer_secret': 'A3IP7wH2pZ0zpiCCCYwO.Z7HkK',
        'user_id': '???',
    },
    'bitly': {
        'consumer_key': 'd4afbd49a8abfbbf288730725dd9609dbb167320',
        'consumer_secret': 'cd30cb160445410d2825aed974ae5fdb15a3db9b',
        'user_id': 'o_a1o5pegh9',
    },
    'deviantart': {
        'consumer_key': '376',
        'consumer_secret': 'd56ec842a9558fe9916210b376988c2d',
    },
    'eventbrite': {
        'consumer_key': 'M5T4QRF5TNIQQJ76EC',
        'consumer_secret': 'C4HNTPVUKCMK3XBWQJ45KFV5H2AIII5C7XNNPZIYSQIQAPMQP7',
        'user_id': '125996068589',
    },
    'facebook': {
        'consumer_key': '482771598445314',
        'consumer_secret': '7163e6e8dedc2c055445b553823ec910',
        'user_id': '737583375',
        'user_password': 'kokotina',
        # This changes when switching from and to Daylight Saving Time
        # 'user_timezone': '2',
    },
    'foursquare': {
        'consumer_key': '11Q4GU3IGQYN3QTR5542VAGE1ZCQD5QDAOXVR1LA3FZ3Q24Z',
        'consumer_secret': 'WN1HYN4W0QJ4H0YV2KET1XKJHA1W2PFQT4WFOKDG3J3T05GK',
        'user_id': '8698379',
        'user_country': u'Slovenská republika',
        'user_picture': 'https://irs2.4sqi.net/img/user/SEG1MMJYH0XHZTSY.jpg',
    },
    'google': {
        'consumer_key': '75167970188.apps.googleusercontent.com',
        'consumer_secret': 'Y70ZmvlkMKOTB8kKGBgN_BME',
        'user_id': '117034840853387702598',
        'user_password': 'google19pitelova79',
        'user_email': 'peterhudec.com@gmail.com',
        'user_locale': 'en',
        'user_picture': ('https://lh5.googleusercontent.com/-LbPepOoFAfA/'
                         'AAAAAAAAAAI/AAAAAAAAOWY/3rWutUjFRGw/photo.jpg?sz=50'),
    },
    'github': {
        'consumer_key': '4dde1fd8f548bfe87f0c',
        'consumer_secret': '6549d450d58f1285fe82cf7a0f1c1dd4316a6644',
        'user_id': '2333157',
        'access_headers': {'User-Agent': ('Authomatic.py Automated Functional '
                                          'Tests')},
    },
    'linkedin': {
        'consumer_key': 'idrh3rkqtgxe',
        'consumer_secret': 'vtae4fUc1plDjPLc',
        'user_id': 'l2mc5sQrfp',
        'user_country': 'Slovak Republic',
        'user_link': 'https://www.linkedin.com/in/phudec',
        'user_picture': ('https://media.licdn.com/mpr/mprx/0_rOHwyzFFkNCtfH3mrMRNyn6eQlbj7wKm-spqynTJMcPDKfbay44b-9zceyFG2ulCAjovPAxWGqj7'),
        'user_phone': PHONE_INTERNATIONAL,
    },
    'paypal': {
        'consumer_key': 'AR58GRBgr81q6vZQOUxwB1OF9_62PXb1CouQVaENf5dbTLgPkr3K7YZXgnc6',
        'consumer_secret': 'EJqCvRAZ4sFobX_NlzyVMyD3PSXH41pAWpeCFpiepworglq_f_5dl3TrCYFl',
    },
    'reddit': {
        'consumer_key': 'Jx3WyR5xS4pm1A',
        'consumer_secret': 'Z0RWV65T5e-qKf0OHDIu1baKhrI',
        'user_login': USERNAME,
        'user_id': 'aurmu',
        'access_headers': {'User-Agent': ('Authomatic.py Automated Functional '
                                          'Tests')}
    },
    # 'viadeo': {
    #     'consumer_key': 'AuthomaticDevNyWlGx',
    #     'consumer_secret': 'NvQuiowaMRBcs',
    # },
    'vk': {
        'consumer_key': '3479081',
        'consumer_secret': '3QKH4U5tpKytUYDGMWbO',
        'user_id': '203822236',
        'user_city': '1908070',
        'user_country': '184',
        'user_gender': '2',
        'user_picture': 'http://cs7010.vk.me/c619226/v619226236/57a1/LJ4KAzr-byY.jpg',
        'user_timezone': '1',
    },
    'windowslive': {
        'consumer_key': '00000000440E8C5B',
        'consumer_secret': 'gu57AluGQnMkzxzdVp0ficFC00pBkl4S',
        'user_id': '5706420657626adb',
    },
    'yammer': {
        'consumer_key': '9JsB3qvVnptaR8GOkfA',
        'consumer_secret': 'Rt11EFemrHIZ6VY8pk8K4CvovTM6Y4hQmo8E3HDKY',
        'user_id': '1496566333',
        'user_picture': ('https://mug0.assets-yammer.com/mugshot/images/48x48/'
                         'gWV0tl9Ln-NvG4V5-1rghnNwzxkBGfbn'),
        'user_timezone': 'Pacific Time (US & Canada)',
        'user_locale': 'en-US',
    },
    'yandex': {
        'consumer_key': '9c77329488b24bc6b8edb66777e1236a',
        'consumer_secret': '4b4408cda2f0459fab278b0880ebcf4d',
        'user_login': USERNAME,
        'user_id': '203067641',
    },
}
