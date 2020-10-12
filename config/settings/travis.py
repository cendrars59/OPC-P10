from . import *

DATABASES = {
    'default': {
        # Using postgresql connector
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pure',  # Database name
        'USER': 'dick',  # Database user name
        'PASSWORD': 'rivers',
        'HOST': 'localhost',
        'PORT': '5432',

    },
}
