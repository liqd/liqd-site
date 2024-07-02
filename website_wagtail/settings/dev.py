from .base import *

DEBUG = True
WAGTAILADMIN_BASE_URL = "http://localhost:8006"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "liqd.net"]

try:
    from .local import *
except ImportError:
    pass

CSP_REPORT_ONLY = True
CSP_DEFAULT_SRC = [
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    "data:",
    "blob:",
    "*",
]
