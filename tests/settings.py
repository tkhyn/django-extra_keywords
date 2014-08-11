DEBUG = True
SECRET_KEY = 'secret'

ROOT_URLCONF = 'tests.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


DATABASES = {
    'default': {
        'NAME': 'extra_keywords',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = ('django_nose',
                  'extra_keywords',
                  'tests.testapp',)

MIDDLEWARE_CLASSES = ()

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
