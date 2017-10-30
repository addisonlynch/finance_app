import os
PROJECT_ROOT = os.path.dirname(__file__)
SECRET_KEY = 'ful6vecf4*z%6#%mkn6zdedmtg8f)d*%5wcp#&=n+4gelbruum'

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['627e203e.ngrok.io',]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'utils',
    'stocks',
    'portfolio',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
DATABASES = {

#    'default': {
#       'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'portfolios',
#        'USER': 'djangouser',
#        'PASSWORD': 'password',
#        'HOST': 'localhost',
#        'PORT': '3306',
 #   },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'portfoliodb',
        'USER': 'djangouser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


TEMPLATES = [{
    'BACKEND' : 'django.template.backends.django.DjangoTemplates',
    'DIRS' : [os.path.join(PROJECT_ROOT, 'templates')],
    'APP_DIRS' : True,
    'OPTIONS' : { 
        'context_processors' : [
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.template.context_processors.request',
        ],
        'debug':DEBUG,

    }
    }
]

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'fixtures'),
)

LOGIN_REDIRECT_URL = '/'


#DATABASE_ROUTERS = ['stocks.routers.StocksDatabaseRouter']
