"""
Django settings for monthly_challenges project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ya4jmf-j6sulfi^z84ah26&0)ys3pfxj!xnj730&*c2fu8v$!('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # if set False, the development server won't work anymore
# it should be set to false on the deployment of application - to see the 404 template we setup

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # add own app to be automatically detected;makes django aware of this app
    # double check that the staticfiles is here to ensure that
    # Django loads the needed functionality to handle static files
    'challenges',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'monthly_challenges.urls'
# DIRS- you can add paths to directories in your folder, where you wanna store the templates
# BASE_DIR / "challenges" / "templates" - django should look in this path when looking for templates

# APP_DIRS- tells django that it wants to look for templates in the app folders; best practice way
# you need to register your app so that it can be automatically detected
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # BASE_DIR / "challenges" / "templates"
            # to ensure that the django also checks the templates folder in the overall project folder
            BASE_DIR / "templates"
        ],
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

WSGI_APPLICATION = 'monthly_challenges.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

#simply tells Django what URL it should serve those static assets
#by default, Django will already look for folders named static in app folders
#and look for static files and will automatically detect and include those
#HOWEVER, it does not look on a global/root level in your main proj
#to make django aware ofstatic on a global level, add new setting, STATICFILES_DIRS
STATIC_URL = 'static/'

#Similar to DIRS of TEMPLATES; Specify the folders that should be considered when
#Django collects and loads static files
STATICFILES_DIRS = [
    BASE_DIR / "static" #tells Django that the static folder in root project directory should also be considered 
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
