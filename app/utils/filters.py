import json

from flask import Blueprint
from markdown2 import Markdown

filters = Blueprint("filters", __name__)


@filters.app_template_filter()
def versioned_asset(filename):
    with open("mix-manifest.json") as file:
        data = json.load(file)

    return data[filename]


@filters.app_template_filter()
def markdown(markdown_text):
    return Markdown().convert(markdown_text)
