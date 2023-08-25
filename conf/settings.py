import math
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
import os, sys

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
SECRET_KEY = 'django-insecure-obnwes9$5-43f03!su!ce1in@gpp+9a-f3am*@xw^sboh)+_qs'
# print(os.getenv('DJANGO_SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = os.getenv('DJANGO_DEBUG')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'users',
    'content',
    'chat',

    # Third party libraries
    'rest_framework',
    'drf_yasg',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'conf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DATABASE_ENGINE'),
#         'NAME': os.getenv('DATABASE_NAME'),
#         'USER': os.getenv('DATABASE_USER'),
#         'PASSWORD': os.getenv('DATABASE_PASSWORD'),
#         'HOST': os.getenv('DATABASE_HOST', default='localhost'),
#         'PORT': os.getenv('DATABASE_PORT')
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'shared.rest_framework.permissions.IsAdminUserOrReadOnly',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ),
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # 'EXCEPTION_HANDLER': 'utils.exceptions.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '10/minute',
    #     'user': '10/minute'
    # }
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Type in the *\'Value\'* input box below: **\'Bearer &lt;JWT&gt;\'**, where JWT is the '
                           'JSON web token you get back when logging in.'
        }
    },
    'PERSIST_AUTH': True
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=2),
    'ALGORITHM': 'HS256',
    'UPDATE_LAST_LOGIN': True,
    # "TOKEN_OBTAIN_SERIALIZER": "apps.shared.rest_framework.CustomTokenObtainPairSerializer",

}

# l = []
# for i in range(1, 16):
#     if i % 7 == 0:
#         l.append("Ronaldu")
#     if i % 10 == 0:
#         l.append("messi")
#
#     else:
#         l.append(i)
# print(l)


# l = [4, 9, 5]
# l2 = [9, 4, 9, 8, 4]
# new = []
#
# for i in l:
#     if i in l2:
#         new.append(i)
# print(new)

# l = ["d", 'o', 'o', 'G']

# a = 32
# while a > 1:
#     print(a)
#     a = a / 2

# from math import log2, floor
# x = int(input("Son kiriting: "))
# a = log2(x)
# if floor(a) == a:
#     print(True)
# else:
#     print(False)

# print(log2(128))
# print(math.floor(4.6))

# l = [1, 2, 3, 1]
#
# if len(set(l)) == len(l):
#     print(False)
# else:
#     print(True)
# s = 'salom'
# print(s)























