from .base import Base


class TestGeneratorApi(Base):
    def test_make_model_file(self):
        body = self.get_test_data('with_no_relations.json')
        r = self.client.post('/field/param', json=body)

