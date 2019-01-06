from flask import request, jsonify
from app import app
from app.helpers import validator, model_generator


@app.route('/field/param', methods=['POST'])
def model_generator_api():
    if request.is_json:
        body = request.data
        keys = ['content_name', 'fields']
        if not body:
            validated = validator.field_validator(keys, {})
            if not validated["success"]:
                return jsonify(validated['data']), 400
        body = request.get_json()
        validated = validator.field_validator(keys, body)
        if not validated["success"]:
            return jsonify(validated['data']), 400
        model_generator.make_file(body)
        return jsonify(message="Success"), 201
    else:
        return jsonify({"message": "Content type is not json"}), 400
