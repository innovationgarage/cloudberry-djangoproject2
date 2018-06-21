"""
Django settings for cloudberry_djangoproject project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os, sys, imp

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qgpmkoirf#l9z$+x4fgt8&v02qyt0vnt%d1!z39v2241ouoc=g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'import_export',
    'django_import_export_cli',
    'django_global_request',
    # extendnetjson: Dependency for django_netjsonconfig that needs to
    # be before 'admin'
    'openwisp_utils.admin_theme',    
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.contenttypes',    
    'registration', #should be immediately above 'django.contrib.admin'
    'cloudberry_accounts',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # extendnetjson: Dependencies for django_netjsonconfig
    'sortedm2m',
    'reversion',
    # 'django_admin_ownership.apps.DjangoAdminOwnershipConfig', #FIXME
    # extendnetjson: This app could be extended the same way as
    # django_netjsonconfig. This has however not been done in this
    # project.
    'django_x509',
    # extendnetjson: Include your extension app here, not
    # django_netjsonconfig itself
    'cloudberry_app',
    'django_freeradius',
    # 'cloudberry_ownership', #FIXME
    'cloudberry_auth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_global_request.middleware.GlobalRequestMiddleware',
]

SECRET_KEY = '_'

SITE_ID = 1

ROOT_URLCONF = 'cloudberry_djangoproject.urls'

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
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
            ],
        },
    },
]

WSGI_APPLICATION = 'cloudberry_djangoproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Django-registration settings
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[Cloudberry App]'
# SEND_ACTIVATION_EMAIL = True
# ACTIVATION_EMAIL_SUBJECT = "Now you can taste the Cloudberry app by Innovation Garage"
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/'

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# email verification
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'igcloudberry@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

REGISTRATION_EMAIL_HTML = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/cloudberry/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# extendnetjson: We need to include the static files from
# django_netjsonconfig manually, as django_netjsonconfig is not in
# INSTALLED_APPS
STATICFILES_DIRS = [os.path.join(imp.find_module("django_netjsonconfig")[1], 'static')]

NETJSONCONFIG_BACKENDS = (
    ('cloudberry_netjson.OpenWrt', 'OpenWRT/Cloudberry'),
    ('netjsonconfig.OpenWrt', 'OpenWRT/LEDE'),
    ('netjsonconfig.OpenWisp', 'OpenWISP Firmware 1.x'))

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

PASSWORD_HASHERS = [
    'cloudberry_auth.password.FreeradiusSHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher'
]

if 'runserver' in sys.argv:
    ROOT = ''
else:
    ROOT = '/cloudberry'

local_settings = os.path.join(os.path.dirname(os.path.dirname(__file__)), "local_settings.py")
if os.path.exists(local_settings):
    with open(local_settings) as f:
        code = compile(f.read(), local_settings, 'exec')
        exec(code, globals(), locals())
