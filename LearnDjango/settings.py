"""
Django settings for LearnDjango project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import configparser
import sys
import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件
config = configparser.RawConfigParser()
config.read(os.path.join(BASE_DIR, 'LearnDjango/config.ini'))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('SECRET_KEY', 'secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
# 一旦把DEBUG设为False之后, runserver服务不再提供静态文件服务
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    # 注册子应用
    # 子应用名.apps.子应用名首字母大写Config
    'rest_framework',
    'django_filters',
    'drf_yasg',

    'projects.apps.ProjectsConfig',
    'interfaces.apps.InterfacesConfig',
    'user.apps.UserConfig',
    'configures.apps.ConfiguresConfig',
    'debugtalks.apps.DebugtalksConfig',
    'envs.apps.EnvsConfig',
    'reports.apps.ReportsConfig',
    'testsuits.apps.TestsuitsConfig',
    'testcases.apps.TestcasesConfig'
]

REST_FRAMEWORK = {
    # 默认响应渲染类
    # 'DEFAULT_RENDERER_CLASSES': (
    #     # json渲染器为第一优先级
    #     'rest_framework.renderers.JSONRenderer',
    #     # 可浏览的API渲染器为第二优先级
    #     'rest_framework.renderers.BrowsableAPIRenderer',
    # ),
    'DEFAULT_FILTER_BACKENDS':['rest_framework.filters.OrderingFilter',
                               'django_filters.rest_framework.backends.DjangoFilterBackend'],
    # 在全局指定分页的引擎
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'utils.pagination.PageNumberPaginationManual',
    'DEFAULT_PAGINATION_CLASS': 'utils.pagination.PageNumberPaginationManual',
    'PAGE_SIZE': 10,
    # 同时必须指定每页显示的条数
    # 'PAGE_SIZE': 3,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
}

JWT_AUTH = {
    # 默认5分钟过期, 可以使用JWT_EXPIRATION_DELTA来设置过期时间
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    # 'JWT_AUTH_HEADER_PREFIX': 'B',
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'utils.jwt_handler.jwt_response_payload_handler',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 4.添加白名单
# CORS_ORIGIN_ALLOW_ALL为True, 指定所有域名(ip)都可以访问后端接口, 默认为False
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST指定能够访问后端接口的ip或域名列表
# CORS_ORIGIN_WHITELIST = [
#     "http://127.0.0.1:8000",
#     "http://localhost:8080",
#     "http://192.168.1.63:8080",
#     "http://localhost:8000",
# ]

# 允许跨域时携带Cookie, 默认为False
CORS_ALLOW_CREDENTIALS = True


ROOT_URLCONF = 'LearnDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'LearnDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        # 指定数据库引擎
        'ENGINE': 'django.db.backends.mysql',
        # 指定数据库名称
        'NAME': config['MysqlDB']['DBName'],
        # 指定数据库用户名
        'USER': config['MysqlDB']['DBUser'],
        # 指定数据库密码
        'PASSWORD': config['MysqlDB']['DBPassword'],
        # 指定数据库的host
        'HOST': config['MysqlDB']['DBHost'],
        # 指定数据库的port
        'PORT': config.getint('MysqlDB', 'DBPort')
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s - [%(levelname)s] - [msg]%(message)s'
        },
        'simple': {
            'format': '%(asctime)s - [%(levelname)s] - %(name)s - [msg]%(message)s - [%(filename)s:%(lineno)d ]'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/mytest.log"),  # 日志文件的位置
            'maxBytes': 100 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'mytest': {  # 定义了一个名为mytest的日志器
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'DEBUG',  # 日志器接收的最低日志级别
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# 测试报告HTML文件所在目录
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

# 测试yaml文件所在目录
SUITES_DIR = os.path.join(BASE_DIR, 'suites')

# 收集静态文件
# 1. 在项目根目录下创建static文件夹
# 2. 执行收集命令: python manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, "front_ends/static")
