from .base import *  # NOQA F403
from .base import env


ALLOWED_HOSTS = []

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
SECRET_KEY = env.str('DJANGO_SECRET_KEY')