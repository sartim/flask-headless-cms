import os
import json

from flask_headless_cms.skeleton.app import app


class Base:
    @classmethod
    def setup_class(cls):
        cls.client = app.test_client()
        cls.no_relation_data = cls.get_test_data('with_no_relations.json')

    @staticmethod
    def get_test_data(file):
        test_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', file))
        with open(test_data_path) as f:
            data = json.load(f)
        return data