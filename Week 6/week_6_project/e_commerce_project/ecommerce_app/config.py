# Import libraries
import os
from datetime import timedelta

# Define base class `Config`
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQL_TRACK_MODIFICATIONS = False

    # JWT Settings
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    # Email Settings
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT',587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')

    # File upload settings
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'png','jpg','jpeg','pdf'}

    ITEMS_PER_PAGE = 10

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SUPPRESS_SEND = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = os.getenv('TEST_DATABASE_URL')
    MAIL_SUPPRESS_SEND = True
    JWT_ACCESS_TOKEN_EXPIRES = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')


# The config dictionary 
config = {
    'development' : DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}




