import json

from flask import Blueprint

filters = Blueprint("filters", __name__)


@filters.app_template_filter()
def versioned_asset(filename):
    with open("mix-manifest.json") as file:
        data = json.load(file)

    return data[filename]
