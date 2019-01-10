import flask
from flask import jsonify
from app.helpers.exceptions import JsonException


def success_js_response(dict_ctx={}, success=True, message=None):
    dict_ctx["success"] = success
    if not success and message is None:
        raise JsonException("must define a message if returning an error")
    else:
        dict_ctx["message"] = message
    return jsonify(dict_ctx), 200



def response_dict(obj, results, path, id=None):
    domain = flask.request.url_root
    if obj.has_next:
        data = {
            "count": obj.total,
            "results": results,
            "next": "{0}{1}?id={2}&page={3}".format(domain, path, id, obj.next_num)
            if id else "{0}{1}?page={2}".format(domain, path, obj.next_num),
            "previous": ""
        }
    elif obj.has_prev:
        data = {
            "count": obj.total,
            "results": results,
            "next": "",
            "previous": "{0}{1}?id={2}&page={3}".format(domain, path, id, obj.prev_num)
            if id else "{0}{1}?page={2}".format(domain, path, obj.prev_num),
        }
    else:
        data = {
            "count": obj.total,
            "results": results,
            "next": "",
            "previous": ""
        }
    return data
