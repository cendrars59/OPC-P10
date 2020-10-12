from . import *

DATABASES = {
    'default': {
        # Using postgresql connector
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pure',  # Database name
        'USER': 'postgres',  # Database user name
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',

    },
}
