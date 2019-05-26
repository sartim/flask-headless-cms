from flask_headless_cms.skeleton.app.helpers import utils
from flask_headless_cms.create_app import template_env


def create_file_dir(package_name):
    file_dir = '{}/app/{}/'.format(utils.working_dir, package_name)
    if utils.create_dir(file_dir):
        return file_dir
    raise OSError


def create_model_package(package_name):
    model_dir = '{}/app/{}/{}'.format(utils.working_dir, package_name, 'models.py')
    if utils.create_dir(model_dir):
        return model_dir
    raise OSError


def _create_field(field, field_list):
    if field['is_primary_key']:
        if field['data_type'] == 'INTEGER':
            field_list.append('{0} = db.Column(db.Integer, primary_key=True)'.format(field['column_name']))
        if field['data_type'] == 'UUID':
            field_list.append('{0} = db.Column(db.String, primary_key=True)'.format(field['column_name']))
    if field['data_type'] == 'VARCHAR':
        if not field['is_null']:
            field_list.append('{0} = db.Column(db.String(255))'.format(field['column_name']))
        field_list.append('{0} = db.Column(db.String(255), nullable=True)'.format(field['column_name']))
    if field['data_type'] == 'TEXT':
        if not field['is_null']:
            field_list.append('{0} = db.Column(db.TEXT)'.format(field['column_name']))
        field_list.append('{0} = db.Column(db.TEXT, nullable=True)'.format(field['column_name']))
    if field['data_type'] == 'BOOLEAN':
        if not field['default']:
            field_list.append('{0} = db.Column(db.Boolean, default=False)'.format(field['column_name']))
        field_list.append('{0} = db.Column(db.Boolean, default=True)'.format(field['column_name']))
    if field['data_type'] == 'JSON':
        if not field['is_null']:
            field_list.append('{0} = db.Column(db.JSON)'.format(field['column_name']))
        field_list.append('{0} = db.Column(db.JSON, nullable=True)'.format(field['column_name']))
    if field['data_type'] == 'TIMESTAMP':
        if not field['is_null']:
            if not field['on_update_default']:
                field_list.append('{0} = db.Column(db.DateTime, default=db.func.current_timestamp())'
                                  .format(field['column_name']))
            field_list.append('{0} = db.Column(db.DateTime, default=db.func.current_timestamp(), '
                              'onupdate=db.func.current_timestamp())'.format(field['column_name']))
        field_list.append('{0} = db.Column(db.DateTime, nullable=True)'.format(field['column_name']))


def _get_attributes(data):
    field_list = []
    for field in data['fields']:
        _create_field(field, field_list)
    join_fields = ";".join(field_list)
    model_fields = join_fields.replace(";", "\n\t")
    return model_fields


def _get_model_params(data):
    field_list = [field['column_name'] for field in data['fields']]
    field_names = ", ".join(field_list)
    return field_names


def _get_declarations(data):
    field_list = []
    for field in data['fields']:
        field_list.append('self.{field_name} = {field_name}'.format(field_name=field['column_name']))
    join_fields = ";".join(field_list)
    repr_fields = join_fields.replace(";", "\n\t\t")
    return repr_fields


def make_file(data):
    package_name = data['content_name'].lower()
    file_dir = create_file_dir(package_name)
    model_dir = create_model_package(package_name)
    model = data['content_name'].capitalize()
    table = data['content_name'].lower()
    template = template_env.get_template('model_from_base.jinja2')
    attributes = _get_attributes(data)
    params = _get_model_params(data)
    declarations = _get_declarations(data)
    template_var = dict(model=model, table=table, attributes=attributes, params=params, declarations=declarations)
    with open(model_dir, 'w') as fd:
        fd.write(template.render(template_var))
    print('Execution completed.')
