"""
Django settings for djangoproject project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z(o%=ylj02*zu-y!lr7c$8&8o3$(_yq(79^5&l#0h%m(2m-peg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


SITE_URL="http://Peerwork.in"

if DEBUG:
    SITE_URL="http://127.0.0.1:8000"


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'books.apps.BooksConfig',
    'users.apps.UsersConfig',
    'account.apps.AccountConfig',
    'search.apps.SearchConfig',
    'friends.apps.FriendsConfig',
    # 'stripe',
    'razorpay',
    'xhtml2pdf',
    'mathfilters',
    'rest_framework',
    'taggit',
    'widget_tweaks',
    'django.contrib.humanize',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'octicons',
    'multiselectfield',
    'phone_field',
    #'notify',
    


]

#taggit
TAGGIT_TAGS_FROM_STRING = 'blog.__init__.comma_splitter'
#TAGGIT_AUTOSUGGEST_CSS_FILENAME = 'autoSuggest-grappelli.css'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoproject.urls'



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


AUTH_USER_MODEL='account.Account'

WSGI_APPLICATION = 'djangoproject.wsgi.application'
    




# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

django_heroku.settings(locals())

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT=os.path.join(BASE_DIR, 'media') #mediaroot is the location where the uploaded pics will be located in the file system
MEDIA_URL='/media/' #mediaurl will create the directory inside the mediaroot and the save the pics there

CRISPY_TEMPLATE_PACK='bootstrap4' #loading the crispy forms in the system

LOGIN_REDIRECT_URL='blog-home' 
LOGOUT_REDIRECT_URL='login'

LOGIN_URL='login' 



#Stripe Settings
if DEBUG:
    # test keys
    STRIPE_PUBLISHABLE_KEY = ''
    STRIPE_SECRET_KEY = ''
    BT_ENVIRONMENT='sandbox'
    BT_MERCHANT_ID='YOUR BT_MERCHANT_ID'
    BT_PUBLIC_KEY='YOUR BT_PUBLIC_KEY'
    BT_PRIVATE_KEY='YOUR BT_PRIVATE_KEY'
else:
    # live keys
    STRIPE_PUBLISHABLE_KEY = 'YOUR STRIPE LIVE PUB KEY'
    STRIPE_SECRET_KEY = 'YOUR STRIPE LIVE SECRET KEY'





#SMTP Configuration
DEFAULT_FROM_EMAIL="Peerwork.in <srk.satyarth.1@gmail.com>"

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='srk.satyarth.1@gmail.com'
EMAIL_HOST_PASSWORD='messiisgod10'



