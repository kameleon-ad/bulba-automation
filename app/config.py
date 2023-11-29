import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    CACHE_TYPE = os.getenv('CACHE_TYPE')
    CACHE_REDIS_HOST = os.getenv('CACHE_REDIS_HOST')
    CACHE_REDIS_PORT = os.getenv('CACHE_REDIS_PORT')
    CACHE_REDIS_DB = os.getenv('CACHE_REDIS_DB')
    CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL')
    CACHE_DEFAULT_TIMEOUT = os.getenv('CACHE_DEFAULT_TIMEOUT')


class ProductionConfig(BaseConfig):
    DEBUG = False


class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = False


class TestingConfig(BaseConfig):
    TESTING = True
