from flask import current_app
from flask_login import current_user


def env():
    return dict({"env": current_app.config["ENV"]})


def app_state():
    logged_in = current_user.is_authenticated if current_user else 0
    is_admin = (
        current_user.has_role("administrator")
        if current_user and current_user.is_authenticated
        else 0
    )
    username = (
        current_user.username
        if current_user and current_user.is_authenticated
        else "My Account"
    )
    email = (
        current_user.email if current_user and current_user.is_authenticated else None
    )
    first_name = (
        current_user.first_name
        if current_user and current_user.is_authenticated
        else None
    )
    last_name = (
        current_user.last_name
        if current_user and current_user.is_authenticated
        else None
    )

    site_default = current_app.config["BLOG_DEFAULT_IMAGE"]
    image_widths = current_app.config["IMAGE_WIDTHS"].split(",")
    tiny_thumbnail_width = current_app.config["TINY_THUMBNAIL_WIDTH"]
    small_thumbnail_width = current_app.config["SMALL_THUMBNAIL_WIDTH"]
    large_thumbnail_width = current_app.config["LARGE_THUMBNAIL_WIDTH"]
    cloudinary_on = current_app.config["CLOUDINARY_ON"]
    cloudinary_account = current_app.config["CLOUDINARY_ACCOUNT"]

    settings = {
        "images": {
            "site_default": site_default,
            "widths": image_widths,
            "thumbnail_widths": {
                "tiny": tiny_thumbnail_width,
                "small": small_thumbnail_width,
                "large": large_thumbnail_width,
            },
            "cloudinary": {
                "on": cloudinary_on,
                "account": cloudinary_account,
            },
        },

    }

    return dict(
        state={
            "user": {
                "logged_in": logged_in,
                "is_admin": is_admin,
                "account": {
                    "username": username,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                },
            },
            "settings": settings
        }
    )
