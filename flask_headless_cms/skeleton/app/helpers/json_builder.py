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



def response_dict(obj, results, path, id=None, **kwargs):
    domain = flask.request.url_root
    if id:
        next_url = "{}{}?id={}".format(domain, path, id)
    elif kwargs:
        next_url = "{}{}?{}={}&page={}".format(domain, path, ' '.join(kwargs.keys()),
                                               kwargs[' '.join(kwargs.keys())], obj.next_num)
    elif not id:
        next_url = "{}{}?page={}".format(domain, path, obj.next_num)

    if kwargs:
        prev_url = "{}{}?{}={}&page={}".format(domain, path, ' '.join(kwargs.keys()),
                                               kwargs[' '.join(kwargs.keys())], obj.prev_num)
    elif not id:
        prev_url = "{0}{1}?page={2}".format(domain, path, obj.prev_num)
    elif id:
        prev_url = "{}{}?id={}&page={}".format(domain, path, id, obj.prev_num)

    if obj.has_next:
        data = dict(count=obj.total, results=results, next=next_url, previous=prev_url if obj.prev_num else "")
    else:
        data = dict(count=obj.total, results=results, next="", previous="")
    return data
