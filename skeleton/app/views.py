from flask import request, jsonify
from app import app
from app.helpers import validator, model_generator


@app.route('/')
def root():
    return "Welcome!"


@app.route('/field/param', methods=['POST'])
def create_field_params():
    body = request.data
    keys = ['model', 'fields']
    if not body:
        validated = validator.field_validator(keys, {})
        if not validated["success"]:
            return jsonify(validated['data'])
    if request.is_json():
        body = request.get_json()
        validated = validator.field_validator(keys, body)
        if not validated["success"]:
            return jsonify(validated['data'])
        model_generator.make_file(body)
    else:
        return jsonify({"message": "Content type is not json"})
