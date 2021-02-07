import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = True
    MONGODB_HOST = "mongodb:27017"
    MONGODB_DB = 'table_db'
    MONGODB_USERNAME = os.getenv('MONGODB_USER')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
