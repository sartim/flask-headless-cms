from flask import request, jsonify
from skeleton.app import app
from skeleton.app.helpers import validator


@app.route('/')
def root():
    return "Welcome!"


@app.route('/field/param', methods=['POST'])
def create_field_params():
    body = request.data
    keys = ['fields']
    if not body:
        validated = validator.field_validator(keys, {})
        if not validated["success"]:
            return jsonify(validated['data'])
    if request.is_json():
        validated = validator.field_validator(keys, body)
        if not validated["success"]:
            return jsonify(validated['data'])
    else:
        return jsonify({"message": "Content type is not json"})
