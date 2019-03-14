from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass

CSP_REPORT_ONLY = True
CSP_DEFAULT_SRC = ["'self'", "'unsafe-inline'", "'unsafe-eval'", 'data:', 'blob:', '*']
