"""
Richard Account
Since 2017-07-01 19：07
1.Build django/Gunicorn/Nginx/Virtualenvg/Python3 envirment 
2.Complete User Model and login /register system
3,Complete User homepage and related page
Done!
"""
import os
DEBUG = False
SITE_ID = 1
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RXD_DIR = os.path.abspath(BASE_DIR)

AUTH_USER_MODEL = 'account.RxdUser'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(RXD_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(RXD_DIR, 'media')

#----Avatar config-----
THUMBNAIL_BASEDIR = ''
AVATAR_SIZE = 120
AVATAR_CROP = 'smart'
AVATAR_QUALITY = 100
AVATAR_SUBSAMPLING = 1

THUMBNAIL_ALIASES = {
    'jack': {
        'avatar': {'size': (50, 50), 'crop': True},
    },
}

INSTALLED_APPS = [
    'easy_thumbnails',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
   #'gunicorn',
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

ROOT_URLCONF = 'rxd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(RXD_DIR, 'templates')],
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

WSGI_APPLICATION = 'rxd.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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


LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

ALLOWED_HOSTS = ['*']

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECRET_KEY = 'brsn37wah@*tddrnv*b!ufeh1dj*a9+)zb%$snh6h$1#k4y8a_'

