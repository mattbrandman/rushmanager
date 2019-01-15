"""
Django settings for rushmanager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

AUTH_USER_MODEL = 'authentication.BrotherUser'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lz=alvono%-*#ork1e7nifb^675+6_hl$lmp7zor6s&p5$k4x0'

# SECURITY WARNING: don't run with debug turned on in production!

TEMPLATE_DEBUG = DEBUG

LOGIN_URL = '/home/'

#Change this once profile views are up and running 
LOGIN_REDIRECT_URL = '/rushtracker/'

CRISPY_FAIL_SILENTLY = not DEBUG

ALLOWED_HOSTS = [
    'www.rushhound.com',
    'rushhound.com',
]
#this is the profile for Users


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_extensions',
    'crispy_forms',
    'rushtracker',
    'comments',
    'events',
    'braces',
    'storages',
    'authentication',
    'organization',
    'rushperiod',
    'tenancy',
    'ranking',
    'rest_framework',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tenancy.middleware.ThreadLocals',
)

STATICFILES_FINDERS = (
'django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
        'authentication.permissions.SameOrganizationPermission',
    ],
    'DEFAULT_FILTER_BACKENDS':('rest_framework.filters.DjangoFilterBackend',)
}

ROOT_URLCONF = 'rushmanager.urls'

WSGI_APPLICATION = 'rushmanager.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                            )

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

ANONYMOUS_USER_ID = None

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASES['default'] = dj_database_url.config(default='postgres://joe@localhost:5432/mydb')

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/



AWS_STORAGE_BUCKET_NAME = 'rushmanagerbucket'
#AWS_ACCESS_KEY_ID = 
#AWS_SECRET_ACCESS_KEY =
AWS_S3_HOST = 's3-us-west-2.amazonaws.com'
AWS_QUERYSTRING_AUTH=True
REDUCED_REDUNDANCY = True
# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_LOCATION = 'static'
#STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
#STATICFILES_STORAGE = 'rushmanager.custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'rushmanager.custom_storages.MediaStorage'
STATIC_URL = '/static/'#"https://%s/" % AWS_S3_CUSTOM_DOMAIN


