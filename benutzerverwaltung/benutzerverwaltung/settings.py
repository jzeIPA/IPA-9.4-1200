"""
Django settings for benutzerverwaltung project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, NestedActiveDirectoryGroupType
import ldap
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@jp(4ef1$8h%bx%t1z^j-fad^p@=&xm^s+j4-z+0(!&=maw^5v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'benutzeraccounts',     #Applikation eingefuegt
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phonenumber_field',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', #fuegt Cookies hinzu
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', #speichert den authentifizierten Benutzer in eine Session
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'benutzerverwaltung.middleware.LoginRequiredMiddleware'
]

ROOT_URLCONF = 'benutzerverwaltung.urls'

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

WSGI_APPLICATION = 'benutzerverwaltung.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Basis Konfiguration
AUTH_LDAP_SERVER_URI = "ldap://192.168.1.12"
AUTH_LDAP_BIND_DN = "LDAP_IPA"
AUTH_LDAP_BIND_PASSWORD = "Roht4kol"
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_DEBUG_LEVEL: 1,
    ldap.OPT_REFERRALS: 0
}


# Standart Parameter setzen
AUTH_LDAP_USER_SEARCH = LDAPSearch("DC=sbvg,DC=ch", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("DC=sbvg,DC=ch", ldap.SCOPE_SUBTREE, "(objectClass=group)")
AUTH_LDAP_GROUP_TYPE = NestedActiveDirectoryGroupType()

# Welche Attribute sollen ausgelesen werden.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
    "title": "title",
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "CN=ipa-users,cn=users,DC=sbvg,DC=ch",
    "is_staff": "CN=ipa-users,cn=users,DC=sbvg,DC=ch",
    "is_superuser": "CN=ipa-users,cn=users,DC=sbvg,DC=ch"
}

# User in der AD sollen immer aktualisiert werden
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# The LDAP class that represents a user.
LDAP_AUTH_OBJECT_CLASS = "inetOrgPerson"

# Use LDAP group membership to calculate group permissions.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache Einstellungen
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  #ueberprueft die Aehnlichkeit zwischen dem Passwort und einer Menge von Attributen des Benutzers
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', #prueft, ob das Passwort eine Mindestlaenge erreicht. Default: 8.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', #ueberprueft, ob das Passwort in einer Liste von allgemeinen Passwoertern vorkommt. Default: Liste von 1000 allgemeinen Passwoertern.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', #ueberprueft, ob das Passwort nicht vollstaendig aus Nummern besteht.
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = 'user:profile'
LOGOUT_REDIRECT_URL = 'user:login'

STATIC_URL = '/static/'

MEDIA_URL = '/assets/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'default/assets')

LOGIN_URL = 'user/login/'

LOGIN_EXEMPT_URLS = (
    r'^user/logout/$',
    r'^user/register/$',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
