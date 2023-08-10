from pathlib import Path
from datetime import datetime, timedelta
import pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-rqh8^#+qi)8fgw0)m8q!-winan-wh3(linthsx(96!!)ar)byd"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    #
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "corsheaders",
    # "rest_framework_simplejwt",
    # "rest_framework_simplejwt.token_blacklist",
    "allauth",
    "allauth.account",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    #
    "apps.accounts",
    "apps.communities",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        "NAME": "tfg",
        "USER": "root",
        "PASSWORD": "Kemikase1",
        "HOST": "localhost",
        "PORT": "3306",
    }
}

AUTH_USER_MODEL = "accounts.CustomUser"

#
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
#     ),
# }

# SIMPLE_JWT = {
#     "AUTH_HEADER_TYPES": ("JWT",),
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
#     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
# }


# REST_USE_JWT = True

SITE_ID = 1

JWT_AUTH_COOKIE = "auth-cookie"

AUTHENTICATION_BACKENDS = [
    "allauth.account.auth_backends.AuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
]

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "apps.accounts.serializers.UserSerializer",
}

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "apps.accounts.serializers.UserRegisterSerializer",
}

# CORS HEADERS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "ETC/GMT+3"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
