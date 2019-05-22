from .base import Base


class TestRootApi(Base):
    def test_function(self):
        r = self.client.get('/')
        assert r.status_code, 200
        assert r.data, b"Welcome!"
