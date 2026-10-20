import os
from pathlib import Path

import dj_database_url
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent


def get_bool_env(var_name, default=False):
    val = os.environ.get(var_name)
    if val is None:
        return default
    return val.strip().lower() in ('true', '1', 'yes', 't', 'y')


# Detect if running in a known production environment (e.g. Render)
IS_RENDER = bool(os.environ.get('RENDER_EXTERNAL_HOSTNAME') or os.environ.get('RENDER'))

# SECURITY WARNING: don't run with debug turned on in production!
# Defaults to safe production behavior (False) in production; defaults to True locally to keep dev workflow frictionless.
DEBUG = get_bool_env('DEBUG', default=not IS_RENDER)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    if DEBUG:
        # Development-only fallback to avoid breaking local workflows
        SECRET_KEY = 'django-insecure-dev-only-local-secret-key-change-in-production'
    else:
        raise ImproperlyConfigured(
            "The SECRET_KEY environment variable must be set in production (when DEBUG=False)."
        )

# ALLOWED_HOSTS: local loopback addresses are always permitted for local development
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '[::1]']

# Automatically append Render external hostname if provided by the platform
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME and RENDER_EXTERNAL_HOSTNAME not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Support additional comma-separated hosts from environment (e.g. custom domains)
ENV_ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
if ENV_ALLOWED_HOSTS:
    for host in ENV_ALLOWED_HOSTS.split(','):
        cleaned_host = host.strip()
        if cleaned_host and cleaned_host not in ALLOWED_HOSTS:
            ALLOWED_HOSTS.append(cleaned_host)


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    'learning.apps.LearningConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'educaps_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'educaps_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    try:
        db_config = dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=not DEBUG)
        if not db_config:
            raise ValueError("Parsed database configuration is empty.")
        DATABASES = {
            'default': db_config
        }
    except Exception as e:
        raise ImproperlyConfigured(f"Invalid or unsupported DATABASE_URL configuration: {e}")
else:
    # Fail fast if running in production on Render without a persistent database
    if not DEBUG and IS_RENDER:
        raise ImproperlyConfigured(
            "DATABASE_URL is required for production on Render. Ephemeral SQLite is not supported."
        )
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'learning.backends.CaseInsensitiveModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i1n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'
# Tells Django where to find our static folder
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# folder where collectstatic will gather all static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Simplified storage setting for Render
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Authentication redirects
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'