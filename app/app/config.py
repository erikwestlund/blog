import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    REDIS_URL = os.getenv('REDIS_URL')
    REDIS_SESSION_PREFIX = os.getenv('REDIS_SESSION_PREFIX')
    DEBUG_TB_INTERCEPT_REDIRECTS = False
