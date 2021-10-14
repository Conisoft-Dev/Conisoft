"""
Django settings for Conisoft project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vktrs(sw1z6#ra@$g&7o5wgdyy!ux@6cvn&)-ab+qcd9h7s))t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'mainApp',
    'storages',
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

ROOT_URLCONF = 'Conisoft.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'Conisoft.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




# Un-Comment to use new User model
"""
    This Completely changes the user authentication and the superusers as well,
    if you uncomment this you will have to create a new superuser.
 """
AUTH_USER_MODEL = 'mainApp.User'

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = BASE_DIR / "staticFiles"

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    str(BASE_DIR.joinpath('static/')),
]


# Azure Storage settings
AZURE_ACCOUNT_NAME = 'testmediastorage'
AZURE_ACCOUNT_KEY = 'ddgHYoCovVAE5W+SMJe61Y8F+xeKTI84cbux2smXfXMF0yBNWiaaue2Nx2kLT824PiqmpYqM1pivsP+DAV+AhQ==' # Must be replaced by your <storage_account_key>
AZURE_CONTAINER = 'media'
AZURE_CONTAINER_URL = 'https://testmediastorage.blob.core.windows.net/media'
AZURE_CONTAINER_SSL = True
AZURE_CONTAINER_SSL_URL= 'https://testmediastorage.blob.core.windows.net/media'
AZURE_URL_EXPIRATION_SECS = 12000
AZURE_URL_EXPIRATION_SECS_SSL = 12000
AZURE_CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=testmediastorage;AccountKey=ddgHYoCovVAE5W+SMJe61Y8F+xeKTI84cbux2smXfXMF0yBNWiaaue2Nx2kLT824PiqmpYqM1pivsP+DAV+AhQ==;EndpointSuffix=core.windows.net'
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'

# MEDIA_LOCATION = "media"

# Image Model Settings
# MEDIA_URL = '/media/' 
# MEDIA_ROOT = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'