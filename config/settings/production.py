from .base import *  # NOQA F403
from .base import env


ALLOWED_HOSTS = []

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = False
SECRET_KEY = env.str(
    'DJANGO_SECRET_KEY',
    'xm3v!qy!y&l3*79@)vm_3j8i9etp9bes1_(%fy_x*t%!$ad2!n',
)
