import pytest
from flask_headless_cms.skeleton.app import app


def test_function():
    client = app.test_client()
    r = client.get('/')
    assert r.status_code, 200
    assert r.data, b"Welcome!"
