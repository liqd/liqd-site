from .base import *

DEBUG = True
WAGTAILADMIN_BASE_URL = "http://localhost:8006"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "liqd.net"]

try:
    import debug_toolbar
except ImportError:
    pass
else:
    INSTALLED_APPS += ("debug_toolbar",)
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
    INTERNAL_IPS = ("127.0.0.1", "localhost")

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
