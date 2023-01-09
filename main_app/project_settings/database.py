from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'hello_django_dev',
#         'USER': 'hello_django',
#         'PASSWORD': 'hello_django',
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }
# DEBUG=1
# SECRET_KEY=foo
# DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
# SQL_ENGINE=django.db.backends.postgresql
# SQL_DATABASE=hello_django_dev
# SQL_USER=hello_django
# SQL_PASSWORD=hello_django
# SQL_HOST=db
# SQL_PORT=5432
# DATABASE=postgres

