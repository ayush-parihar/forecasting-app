from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
 
SECRET_KEY = "django-insecure-dev-only"          # swap in env var for prod
DEBUG = True
ALLOWED_HOSTS = ["*"]                            # allow localhost
 
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "forecaster",
]
 
MIDDLEWARE = ["django.middleware.common.CommonMiddleware"]
 
ROOT_URLCONF = "forecast_site.urls"
 
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "forecaster" / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.debug",
    ]},
}]
 
WSGI_APPLICATION = "forecast_site.wsgi.application"
STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"