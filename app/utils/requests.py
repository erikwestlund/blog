from flask import request


def request_is_ajax():
    if "X-Requested-With" not in request.headers:
        return False
    else:
        return request.headers["X-Requested-With"].lower() == "xmlhttprequest"


def request_wants_json():
    return request_is_ajax()
