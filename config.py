import os
basedir = os.path.abspath(os.path.dirname(__file__))

os.environ["DEV_DATABASE_URI"] = "mysql+pymysql://root:QWERop[]2016@106.52.209.84:3306/baidi?charset=utf8mb4"
os.environ["TEST_DATABASE_URI"] = "mysql+pymysql://root:QWERop[]2016@106.52.209.84:3306/baidi_test?charset=utf8"
PROJECT_NAME = "baidi"
PER_PAGE = 10
TIME_OUT = 5
FILE_DOWNLOAD_PATH = os.path.abspath(os.path.dirname(__file__)).split(PROJECT_NAME)[0] + PROJECT_NAME + \
                     "/download_files/"

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or  \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
