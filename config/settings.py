
from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
env = environ.Env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("LMAPI_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("LMAPI_DEBUG") == 'True'


if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = env("LMAPI_ALLOWED_HOST").split(',')
    


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
    'license',
    'drf_yasg',
    'common',
    'django_recaptcha', 
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        },
        'Basic': {
            'type': 'basic',
            'description': 'Basic HTTP Authentication'
        }
    },
    'PERSIST_AUTH': True,
    'REFETCH_SCHEMA_WITH_AUTH': True,
    'CODEGEN_URL': 'license:schema-json',
    'USE_SESSION_AUTH': False,  
    'APIS_SORTER': 'alpha',     
    'OPERATIONS_SORTER': 'alpha',
    'TAGS_SORTER': 'alpha',
    'DOC_EXPANSION': 'list',    
    'DEFAULT_MODEL_RENDERING': '',    
    'DEFAULT_MODEL_SCHEMA': '',
    'SPEC_URL' : 'license:schema-json',   
    'VALIDATOR_URL': None,
    'DISPLAY_OPERATION_ID': True,
    'JSON_EDITOR': True,
    'SHOW_EXTENSIONS': True,
    'DEFAULT_EXTENSIONS': [
        'OpenAPIClientCodegen'
    ],
    # 'CONFIG_URL': 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@4.0.0/swagger-ui.css',
    
}

REDOC_SETTINGS = {
    'CODEGEN_URL': 'license:schema-json',
    'SPEC_URL': 'license:schema-json',
    'USE_SESSION_AUTH': False,  # Disable Django login button
    'NO_AUTO_AUTH': True,  
    # 'codegen': {
    #     'enabled': True,
    #     'languages': ['python', 'java', 'php', 'javascript'],  # Add more languages as needed
    # },
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',        
        'NAME': env("LMAPI_DB_NAME"),
        'USER': env("LMAPI_DB_USER"),
        'PASSWORD': env("LMAPI_DB_PASSWORD"),
        'HOST': env("LMAPI_DB_HOST"),
        'PORT': env("LMAPI_DB_PORT"),
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
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

AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  
    
    RECAPTCHA_PUBLIC_KEY = str('6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI')
    RECAPTCHA_PRIVATE_KEY = str('6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe')
    RECAPTCHA_DOMAIN = 'www.recaptcha.net'
    SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']   
    
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    PREPEND_WWW =True
    X_FRAME_OPTIONS = 'SAMEORIGIN'
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_HOST = True
    SESSION_COOKIE_HTTPONLY = True
    
    RECAPTCHA_PUBLIC_KEY = env("LMAPI_RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = env("LMAPI_RECAPTCHA_PRIVATE_KEY")
 
    
    # RECAPTCHA_DOMAIN = 'www.recaptcha.net'
    SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']
    

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_FROM_EMAIL = env("LMAPI_DEFAULT_FROM_EMAIL")
EMAIL_HOST = env("LMAPI_EMAIL_HOST")
EMAIL_PORT= env("LMAPI_EMAIL_PORT")
EMAIL_HOST_USER = env("LMAPI_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("LMAPI_EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS=False
EMAIL_USE_SSL=True
ADMIN_EMAIL = env("LMAPI_ADMIN_EMAIL")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
