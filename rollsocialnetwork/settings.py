"""
roll social network settings.
"""

import json
from pathlib import Path
from decouple import config  # type: ignore[import-untyped]
import dj_database_url
import corsheaders.defaults

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-q=u8&7w8!%khn7a$lj5drzm9i)k90fh7m_-0b14pjxfz51d(ah"
)
DEBUG = config("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*", cast=str.split)
INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    "phonenumber_field",
    "easy_thumbnails",
    "corsheaders",
    "channels",
    "rollsocialnetwork",
    "rollsocialnetwork.phone_auth",
    "rollsocialnetwork.social",
    "rollsocialnetwork.timeline",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "rollsocialnetwork.social.middleware.CurrentUserProfileMiddleware",
    "csp.middleware.CSPMiddleware",
]
ROOT_URLCONF = "rollsocialnetwork.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "./rollsocialnetwork/templates",
            "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "rollsocialnetwork.context_processors.is_home_site",
                "rollsocialnetwork.context_processors.footer_urls",
                "rollsocialnetwork.social.context_processors.social",
            ],
        },
    },
]
WSGI_APPLICATION = "rollsocialnetwork.wsgi.application"
ASGI_APPLICATION = "rollsocialnetwork.asgi.application"
DATABASES = {
    "default": dj_database_url.parse(config("DATABASES_DEFAULT", default="sqlite:///./db.sqlite3"))
}
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
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "rollsocialnetwork.phone_auth.backends.PhoneAuthBackend",
]
LOGIN_REDIRECT_URL = "/t/"
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = "/phone-auth/request/"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = config("STATIC_URL",
                    default="static/")
STATICFILES_DIRS = [
    "frontend/dist",
    "rollsocialnetwork/static",
]
STATIC_ROOT = config("STATIC_ROOT",
                     default=None)
MEDIA_ROOT = config("MEDIA_ROOT", default="./media/")
MEDIA_URL = config("MEDIA_URL", default="/media/")
MEDIA_PATH_AS_STATIC = config("MEDIA_PATH_AS_STATIC",
                              default=False,
                              cast=bool)
MEDIA_PATH_AS_NGINX_ACCEL = config("MEDIA_PATH_AS_NGINX_ACCEL",
                                   default=False,
                                   cast=bool)
NGINX_ACCEL_REDIRECT_INTERNAL_LOCATION = config("NGINX_ACCEL_REDIRECT_INTERNAL_LOCATION",
                                                default="/medias/")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SITE_ID = config("SITE_ID", default=None, cast=lambda v: None if v is None else int(v))
HOME_SITE_ID = config("HOME_SITE_ID", default=1, cast=int)
PHONE_AUTH_VALIDATION_CODE_TTL = config("PHONE_AUTH_VALIDATION_CODE_TTL", default=60, cast=int)
PHONE_AUTH_VALIDATION_CODE_LENGTH = config("PHONE_AUTH_VALIDATION_CODE_LENGTH", default=4, cast=int)
PHONE_AUTH_VERIFY_ATTEMPTS = config("PHONE_AUTH_VERIFY_ATTEMPTS", default=3, cast=int)
PHONE_AUTH_SMS_GATEWAY = config("PHONE_AUTH_SMS_GATEWAY", default="logger")
PHONE_AUTH_SMS_GATEWAY_ARGS = config("PHONE_AUTH_SMS_GATEWAY_ARGS", default="", cast=str.split)
CREATE_USER_PROFILE_URL = "/s/create-user-profile/"
THUMBNAIL_ALIASES = {
    'timeline': {
        'photo8': {
            'size': (8, 8),
            'crop': True,
            'upscale': True,
            'quality': 10,
        },
        'photo184': {
            'size': (184, 184),
            'crop': True,
            'upscale': True,
            'quality': 50,
        },
        'photo584': {
            'size': (584, 584),
            'crop': True,
            'upscale': True,
            'quality': 90,
        },
    }
}
THUMBNAIL_DEFAULT_STORAGE = config("THUMBNAIL_DEFAULT_STORAGE",
                                   default="easy_thumbnails.storage.ThumbnailFileSystemStorage")
CORS_ALLOW_ALL_ORIGINS = config("CORS_ALLOW_ALL_ORIGINS",
                                default=False,
                                cast=bool)
CORS_ALLOWED_ORIGIN_REGEXES = config("CORS_ALLOWED_ORIGIN_REGEXES",
                                     default="",
                                     cast=lambda value: value.split(","))
CORS_ALLOW_HEADERS = [
    *corsheaders.defaults.default_headers,
    "action-component",
]
CORS_ALLOW_CREDENTIALS = True
SECURE_CROSS_ORIGIN_OPENER_POLICY = "unsafe-none"
SESSION_COOKIE_DOMAIN = config("SESSION_COOKIE_DOMAIN",
                               default=None)
CSP_CONNECT_SRC = config("CSP_CONNECT_SRC",
                         default="'self'",
                         cast=lambda value: value.split(","))
CSP_SCRIPT_SRC = config("CSP_SCRIPT_SRC",
                        default="'self','unsafe-eval'",
                        cast=lambda value: value.split(","))
CSP_STYLE_SRC = config("CSP_STYLE_SRC",
                       default="'self','unsafe-hashes',fonts.googleapis.com",
                       cast=lambda value: value.split(","))
CSP_FONT_SRC = config("CSP_FONT_SRC",
                      default="'self',fonts.gstatic.com",
                      cast=lambda value: value.split(","))
CSP_IMG_SRC = config("CSP_IMG_SRC",
                     default="'self'",
                     cast=lambda value: value.split(","))
STORAGES = {
    "default": {
        "BACKEND": config("STORAGES_DEFAULT_BACKEND",
                          default="django.core.files.storage.FileSystemStorage"),
        "OPTIONS": config("STORAGES_DEFAULT_OPTIONS",
                          default="{}",
                          cast=json.loads)
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
    },
    "posts": {
        "BACKEND": config("STORAGES_POSTS_BACKEND",
                          default="django.core.files.storage.FileSystemStorage"),
        "OPTIONS": config("STORAGES_POSTS_OPTIONS",
                          default="{}",
                          cast=json.loads)
    }
}
FTP_STORAGE_LOCATION = config("FTP_STORAGE_LOCATION",
                              default=None)
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": config("CHANNEL_LAYERS_DEFAULT_BACKEND",
                          default="channels.layers.InMemoryChannelLayer"),
        "CONFIG": config("CHANNEL_LAYERS_DEFAULT_CONFIG",
                         default="{}",
                         cast=json.loads)
    }
}
SUBDOMAIN_BASE = config("SUBDOMAIN_BASE",
                        default="roll.local")
ABOUT_PAGE_URL = config("ABOUT_PAGE_URL",
                        default=f"//{SUBDOMAIN_BASE}#about")
TERMS_PAGE_URL = config("TERMS_PAGE_URL",
                        default=f"//{SUBDOMAIN_BASE}#terms")
