import os
from distutils.util import strtobool

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SERVER_NAME = os.getenv("SERVER_NAME")
    ENV = os.getenv("ENV")

    BLOG_TITLE = os.getenv("BLOG_TITLE")
    BLOG_ADMIN_EMAIL = os.getenv("BLOG_ADMIN_EMAIL")

    ADMIN_INIT_USERNAME = os.getenv("ADMIN_INIT_USERNAME")
    ADMIN_INIT_PASSWORD = os.getenv("ADMIN_INIT_PASSWORD")
    ADMIN_INIT_EMAIL = os.getenv("ADMIN_INIT_EMAIL")

    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

    FILE_STORAGE_PROVIDER = os.getenv("FILE_STORAGE_PROVIDER")

    CLOUDINARY_ON = strtobool(os.getenv("CLOUDINARY_ON"))
    CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")
    CLOUDINARY_ACCOUNT = os.getenv("CLOUDINARY_ACCOUNT")

    B2_KEY_ID = os.getenv("B2_KEY_ID")
    B2_APPLICATION_KEY = os.getenv("B2_APPLICATION_KEY")
    B2_BUCKET = os.getenv("B2_BUCKET")
    B2_URL_BASE = os.getenv("B2_URL_BASE")

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION")
    AWS_S3_USING_CDN = strtobool(os.getenv("AWS_S3_USING_CDN"))
    AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
    AWS_S3_URL_BASE = os.getenv("AWS_S3_URL_BASE")

    UPLOAD_DIR = os.getenv("UPLOAD_DIR")
    UPLOAD_ALLOWED_EXTENSIONS = set(os.getenv("UPLOAD_ALLOWED_EXTENSIONS").split(","))

    REDIS_URL = os.getenv("REDIS_URL")
    REDIS_SESSION_PREFIX = os.getenv("REDIS_SESSION_PREFIX")

    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    POST_SNIPPET_LENGTH = int(os.getenv("POST_SNIPPET_LENGTH"))
    POSTS_PER_PAGE = int(os.getenv("POSTS_PER_PAGE"))
    PAGINATE_DEFAULT = int(os.getenv("PAGINATE_DEFAULT"))
    IMAGE_WIDTHS = os.getenv("IMAGE_WIDTHS")
    TINY_THUMBNAIL_WIDTH = int(os.getenv("TINY_THUMBNAIL_WIDTH"))
    SMALL_THUMBNAIL_WIDTH = int(os.getenv("SMALL_THUMBNAIL_WIDTH"))
    LARGE_THUMBNAIL_WIDTH = int(os.getenv("LARGE_THUMBNAIL_WIDTH"))
