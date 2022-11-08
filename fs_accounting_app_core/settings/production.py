from fs_accounting_app_core.settings.common import *
import os
import environ
from pathlib import Path


# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('PROD_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST') + "," + env('DB_PORT'),
        'PORT': env('DB_PORT'),
        'OPTIONS': {
            'ssl': {'ca': os.path.join(os.path.dirname(__file__), 'DigiCertGlobalRootCA.crt.pem')},
            'driver': 'ODBC Driver 18 for SQL Server',
            }
    }     
}

EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')












