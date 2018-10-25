"""
Django settings for webvirtcloud project.

"""

import os
import ldap
from django_auth_ldap.config import LDAPSearch,NestedActiveDirectoryGroupType
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'f72c165f-132f-4b65-a602-92c84f84ca4d'

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'computes',
    'console',
    'networks',
    'storages',
    'interfaces',
    'instances',
    'secrets',
    'logs',
    'accounts',
    'create',
    'datasource',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
    #'django.contrib.auth.backends.RemoteUserBackend',
    #'accounts.backends.MyRemoteUserBackend',
)

AUTH_LDAP_GLOBAL_OPTIONS = {
  ldap.OPT_X_TLS_REQUIRE_CERT: os.getenv('LDAP_TLS_REQUIRE_CERT', False),
  ldap.OPT_X_TLS_DEMAND: os.getenv('LDAP_TLS_DEMAND', False),
  ldap.OPT_REFERRALS: os.getenv('LDAP_REFERRALS', False),
  ldap.OPT_X_TLS_CACERTFILE: "/srv/webvirtcloud/data/ca-certificates.crt",
}

AUTH_LDAP_SERVER_URI = os.getenv('LDAP_SERVER_URI', 'ldap://server')
AUTH_LDAP_BIND_DN = os.getenv('LDAP_BIND_DN', 'CN=ldapuser,OU=Users,DC=example,DC=com')
AUTH_LDAP_BIND_PASSWORD = os.getenv('LDAP_BIND_PASSWORD', 'password')
AUTH_LDAP_USER_SEARCH = LDAPSearch(os.getenv('LDAP_USER_SEARCH', 'OU=Users,DC=example,DC=com'),
    ldap.SCOPE_SUBTREE, "(samAccountName=%(user)s)")
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(os.getenv('LDAP_GROUP_SEARCH', 'OU=Groups,DC=example,DC=com'),
    ldap.SCOPE_SUBTREE, "(objectClass=group)"
)
AUTH_LDAP_GROUP_TYPE = NestedActiveDirectoryGroupType()

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": ["CN=grouptopermit1,OU=Groups,DC=example,DC=com", "CN=grouptopermit2,OU=Groups,DC=example,DC=com"],
    "is_staff": "CN=grouptopermit2,OU=groups,DC=example,DC=com",
    "is_superuser": os.getenv('LDAP_USER_FLAGS_BY_GROUP_SUPERUSER', 'CN=grouptopermit3,OU=groups,DC=example,DC=com')
}

LOGIN_URL = '/accounts/login'

ROOT_URLCONF = 'webvirtcloud.urls'

WSGI_APPLICATION = 'webvirtcloud.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data/db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates'), ],
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

## WebVirtCloud settings

# Websock port
WS_PORT = 6080

# Websock host
WS_HOST = '0.0.0.0'

# Websock public host
WS_PUBLIC_HOST = None

# Websock public port
WS_PUBLIC_PORT = 80

# Websock public path
WS_PUBLIC_PATH = '/novncd/'

# Websock SSL connection
WS_CERT = None

# list of console types
QEMU_CONSOLE_TYPES = ['vnc', 'spice']

# default console type
QEMU_CONSOLE_DEFAULT_TYPE = 'vnc'

# list of console listen addresses
QEMU_CONSOLE_LISTEN_ADDRESSES = (
    ('127.0.0.1', 'Localhost'),
    ('0.0.0.0', 'All interfaces'),
)

# list taken from http://qemu.weilnetz.de/qemu-doc.html#sec_005finvocation
QEMU_KEYMAPS = ['ar', 'da', 'de', 'de-ch', 'en-gb', 'en-us', 'es', 'et', 'fi',
                'fo', 'fr', 'fr-be', 'fr-ca', 'fr-ch', 'hr', 'hu', 'is', 'it',
                'ja', 'lt', 'lv', 'mk', 'nl', 'nl-be', 'no', 'pl', 'pt',
                'pt-br', 'ru', 'sl', 'sv', 'th', 'tr']

# keepalive interval and count for libvirt connections
LIBVIRT_KEEPALIVE_INTERVAL = 5
LIBVIRT_KEEPALIVE_COUNT = 5

ALLOW_INSTANCE_MULTIPLE_OWNER = True
NEW_USER_DEFAULT_INSTANCES = []
CLONE_INSTANCE_DEFAULT_PREFIX = 'instance'
CLONE_INSTANCE_AUTO_NAME = False
LOGS_PER_PAGE = 100
QUOTA_DEBUG = False
ALLOW_EMPTY_PASSWORD = True
SHOW_ACCESS_ROOT_PASSWORD = False
SHOW_ACCESS_SSH_KEYS = False
SHOW_PROFILE_EDIT_PASSWORD = False

# available: default (grid), list
VIEW_ACCOUNTS_STYLE = 'grid'

INSTANCE_VOLUME_DEFAULT_FORMAT = 'qcow2'
INSTANCE_VOLUME_DEFAULT_BUS = 'virtio'
INSTANCE_VOLUME_DEFAULT_CACHE = 'directsync'
