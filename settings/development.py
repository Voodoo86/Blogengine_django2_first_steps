from settings.base import *
from settings.local_settings import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'NAME': os.path.join(BASE_DIR, db_name),
    }
}