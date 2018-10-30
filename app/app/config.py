import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    SERVER_NAME = os.getenv('SERVER_NAME')

    ADMIN_INIT_USERNAME = os.getenv('ADMIN_INIT_USERNAME')
    ADMIN_INIT_PASSWORD = os.getenv('ADMIN_INIT_PASSWORD')
    ADMIN_INIT_EMAIL = os.getenv('ADMIN_INIT_EMAIL')

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    REDIS_URL = os.getenv('REDIS_URL')
    REDIS_SESSION_PREFIX = os.getenv('REDIS_SESSION_PREFIX')

    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

    DEBUG_TB_INTERCEPT_REDIRECTS = False
