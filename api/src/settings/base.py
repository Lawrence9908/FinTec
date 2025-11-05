from pathlib import Path
from dotenv import load_dotenv
from os import getenv, path
from loguru import logger
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

APP_DIR = BASE_DIR  / "core_apps"

local_env_file  = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)

DJANGO_APP = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
]

LOCAL_APPS = [
 "core_apps.common",
 "core_apps.cards",
 "core_apps.user_auth",
 "core_apps.user_profile",
 "core_apps.accounts"
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_countries',
    'phonenumber_field',
    'drf_spectacular',
    'djoser',
    'cloudinary',
    'django_filters',
    'djcelery_email',
    'django_celery_beat',
]

INSTALLED_APPS = DJANGO_APP + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APP_DIR / "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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

# argon2 password hasher
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = True

USE_TZ = True


SITE_ID = 1

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR / "staticfiles")

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# DISABLING DEFUALT DJANGOR LOGGER

LOGGING_CONFIG = None

# LOGURU LOGGER
LOGURU_LOGGING  = {
    "handlers":[
        {
            "sink": BASE_DIR / 'logs/debug.log',
            "level": "DEBUG",
            "filter": lambda  record: record["level"].no <= logger.level("WARNING").no,
            "format": "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: < 8} | {name}:{function}:{line} - {message}",
            "rotation": "10MB",
            "retention": "30 days",
            "compression": "zip",
        },
        {
            "sink": BASE_DIR / 'logs/error.log',
            "level": "DEBUG",
            "format": "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: < 8} | {name}:{function}:{line} - {message}",
            "rotation": "10MB",
            "retention": "30 days",
            "compression": "zip",
            "backtrace": True,
            "diagnose": True
        },
    ]
}

logger.configure(**LOGURU_LOGGING)

LOGGING = {
    "version":1,
    "disabled_existing_loggers": False,
    "handlers":  {"loguru": {"class": "interceptor.InterceptHandler"}},
    "root": {"handlers": ["loguru"], "level":"BEBUG"}
}

