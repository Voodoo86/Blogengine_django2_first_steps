import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

secret_key = '0mp-w)_i!j59a6@k)gc6rl6)7t$eo5czo_5c!cr6ci*snx*-150&rt7h7gjn5dgb5_1!'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
