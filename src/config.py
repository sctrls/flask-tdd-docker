import os  # new


class BaseConfig:
    TESTING = False
    SECRET_KEY = 'my_precious'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    # fix for sqlalchemy 14 not supporting postgres://
    url = os.environ.get('DATABASE_URL')
    if url is not None and url.startswith('postgres://'):
        url = url.replace('postgres://', 'postgresql://', 1)

    SQLALCHEMY_DATABASE_URI = url
