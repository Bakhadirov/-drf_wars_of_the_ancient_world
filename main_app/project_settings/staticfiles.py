import os

from main_app.settings import BASE_DIR

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
