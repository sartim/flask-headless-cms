import os

from flask_headless_cms.create_app import template_env, cwd


def create_api(data, api_route, api_name, model_instance, path):
    model = data['content_name'].capitalize()

    template = template_env.get_template('function_based_api.jinja2')
    template_var = dict(api_route=api_route, api_name=api_name, model=model, model_instance=model_instance)

    with open(os.path.join(path, '.py'), 'w') as fd:
        fd.write(template.render(template_var))


def make_file(data):
    model_package = data['content_name'].lower()
    file_dir = '{}/app/{}/'.format(cwd, model_package)
    file_path = '{}/app/{}/{}'.format(cwd, model_package, '{}.py'.format(data['content_name'].lower()))

    try:
        os.mkdir(file_dir)
    except OSError:
        print("Creation of the directory %s failed" % file_dir)
    else:
        print("Successfully created the directory %s" % file_dir)

    create_api(data, file_path)
    print('Execution completed.')
