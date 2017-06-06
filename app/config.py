import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SMS_API_HOST = r'http://sms-api.luosimao.com/v1/send.json'
SMS_API_KEY = r'key-4efc7922b1bc90b949a2fa073519eb61'


class Config:
    SECRET_KEY = 'xsm secret key'


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'xsm secret key for development'
    MONGODB_SETTINGS = {
        'db': 'development_mongodb',
        'host': 'localhost',
        'port': 27017,
        'username': 'root',
        'password': 'root'
    }


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'xsm secret key for production'
    MONGODB_SETTINGS = {
        'db': 'production_mongodb',
        'host': 'localhost',
        'port': 27017,
        'username': 'root',
        'password': 'root'
    }


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
