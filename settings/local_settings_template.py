import os

# Default Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Default Sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Add value
secret_key = ''
