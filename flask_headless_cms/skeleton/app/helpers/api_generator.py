import os
import textwrap

working_dir = os.getcwd()

class ApiCreator:
    @classmethod
    def get_model_fields(cls, data):
        pass

    @classmethod
    def api_file(cls, model_fields, model, table, data):
        return "from flask.views import MethodView\n" \
               "from app.core.models import Base\n" \
               "\n\nclass {api_name}_api(MethodView):\n\t" \
               "def get(self):\n\n\t" \
               "pass\n\n\t" \
               "def post(self):\n\n\t" \
               "pass".format(api_name=data['content_name'])


def create_model(data, file_path):
    with open(file_path, 'w') as f:
        model_fields = ApiCreator.get_model_fields(data)
        model = data['content_name'].capitalize()
        table = data['content_name'].lower()
        output = ApiCreator.api_file(model_fields, model, table, data)
        f.write(textwrap.dedent(output))

def make_file(data):
    model_package = data['content_name'].lower()
    file_dir = '{}/app/{}/'.format(working_dir, model_package)
    file_path = '{}/app/{}/{}'.format(working_dir, model_package, '{}.py'.format(data['content_name'].lower()))

    try:
        os.mkdir(file_dir)
    except OSError:
        print("Creation of the directory %s failed" % file_dir)
    else:
        print("Successfully created the directory %s" % file_dir)

    create_model(data, file_path)
    print('Execution completed.')