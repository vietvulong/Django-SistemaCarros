"""
Django settings for SistemaCarros project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import django_heroku
import dj_database_url
from decouple import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a^bzz$c36-ei(c&ja_#(9kzh@^x2w6z=koo*$jy6s1r&3yv$uj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

MESSAGE_STORAGE="django.contrib.messages.storage.cookie.CookieStorage"

# Application definition

INSTALLED_APPS = [
    "corsheaders",
    'carros.apps.CarrosConfig',
    'Presupuestos.apps.PresupuestosConfig',
    'ClienteEmpresas.apps.ClienteempresasConfig',
    'Clientes.apps.ClientesConfig',
    'ManoObra.apps.ManoobraConfig',
    'Parte.apps.ParteConfig',
    'Pagos.apps.PagosConfig',
    'InformacionTiendas.apps.InformaciontiendasConfig',
    'ReporteGanancias.apps.ReportegananciasConfig',
    'Usuarios.apps.UsuariosConfig',
    'Detalle.apps.DetalleConfig',
    'Foto.apps.FotoConfig',
    'inventory.apps.InventoryConfig',
    'dashboard.apps.DashboardConfig',
    'invoices.apps.InvoicesConfig',
    'tecnicos.apps.TecnicosConfig',
    'django.contrib.admin',
    'dynamic_formsets',
    'ckeditor',
    'widget_tweaks',
    'mathfilters',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'

]
CORS_ALLOW_ALL_ORIGINS = True


ROOT_URLCONF = 'SistemaCarros.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'SistemaCarros/templates')],
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


#Rich Field

DJRICHTEXTFIELD_CONFIG = {
    'js': ['//cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link image',
        'toolbar': 'bold italic | link image | removeformat',
        'width': 700
    }
}



WSGI_APPLICATION = 'SistemaCarros.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'sistemacarros_db',
        'USER':'postgres',
        'PASSWORD':'admin',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)
STATICFILES_DIRS=(os.path.join(BASE_DIR,'SistemaCarros/static'),)
STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
LOGIN_REDIRECT_URL='dashboard:dashboard'
LOGIN_URL='login'
# MEDIA_ROOT=os.path.join(BASE_DIR,'static/fotos')
MEDIA_ROOT=os.path.join(BASE_DIR,'media/uploads')
MEDIA_URL='/media/uploads/'


# TEMPLATE_DIRS = (
#     os.path.join(os.path.dirname(__file__), 'templates'),
# )
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


django_heroku.settings(locals())



