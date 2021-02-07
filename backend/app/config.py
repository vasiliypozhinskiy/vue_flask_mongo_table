import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = True
    MONGODB_DB = 'table-app'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = os.getenv('MONGODB_USER')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
