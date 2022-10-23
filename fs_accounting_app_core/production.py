import os
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_DATABASE'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}







