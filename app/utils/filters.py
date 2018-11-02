import json

from flask import Blueprint

utils = Blueprint('utils', __name__)


@utils.app_template_filter()
def versioned_asset(filename):
    with open('mix-manifest.json') as file:
        data = json.load(file)

    return data[filename]