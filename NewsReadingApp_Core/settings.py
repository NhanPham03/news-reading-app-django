"""
Django settings for NewsReadingApp_Core project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'quykuro1234567890@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv('PASSAPP')
DEFAULT_FROM_EMAIL = 'quykuro1234567890@gmail.com'



# Build paths inside the project like this: BASE_DIR / 'subdir'.
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv('SECRET_KEY')
SECRET_KEY = "django-insecure-7$p0e3z1(d1peg=&ltrzc2if97oxa9on+efat2=j9y!y87mql&"

# SECURITY WARNING: don't run with debug turned on in production!
# ENV = os.getenv('ENV', 'development')
ENV="development"

if ENV == 'production':
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'news-reading-app-django.onrender.com', '192.168.56.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'corsheaders',

    # Required apps
    'apps.roles',
    'apps.users',
    #'apps.notifications',
    'apps.articles',
    'apps.comments',
    'apps.commissions',
    'apps.commission_user',
    'apps.login',
    'apps.followers',
    'apps.ratings',
    #'apps.category',
    'apps.notify',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:*',
    'http://127.0.0.1:8000',
    'http://localhost:5555',
    'ws://127.0.0.1:56421',
]

ROOT_URLCONF = 'NewsReadingApp_Core.urls'

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

WSGI_APPLICATION = 'NewsReadingApp_Core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# MONGODB_NAME = os.getenv('MONGODB_NAME')
# MONGODB_URI = os.getenv('MONGODB_URI')
# MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
# MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_NAME="news_reading_app"
MONGODB_URI="mongodb+srv://cluster0.7pkab72.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0/"
MONGODB_USERNAME="trg552003"
MONGODB_PASSWORD="trg552003"

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': MONGODB_NAME,
        'CLIENT': {
            'host': MONGODB_URI,
            'username': MONGODB_USERNAME,
            'password': MONGODB_PASSWORD,
        },
    },
}

# JWT authentication settings
AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

# Other project-specific settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
