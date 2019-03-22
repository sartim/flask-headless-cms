import os
import textwrap

working_dir = os.getcwd()

class ModelCreator:
    @classmethod
    def get_fields_names(cls, data):
        field_list = []
        for field in data['fields']:
            field_list.append(field['column_name'])
        field_names = ", ".join(field_list)
        return field_names

    @classmethod
    def get_model_fields(cls, data):
        field_list = []
        for field in data['fields']:
            if field['is_primary_key']:
                if not field['data_type'] == 'UUID':
                    field_list.append('{0} = db.Column(db.String, primary_key=True)'.format(field['column_name']))
            if not field['is_primary_key']:
                if field['data_type'] == 'INTEGER':
                    if not field['is_null']:
                        field_list.append('{0} = db.Column(db.Integer, nullable=False)'.format(field['column_name']))
                    else:
                        field_list.append('{0} = db.Column(db.Integer, nullable=True)'.format(field['column_name']))
                if field['data_type'] == 'VARCHAR':
                    if not field['is_null']:
                        field_list.append('{0} = db.Column(db.String(255))'.format(field['column_name']))
                    else:
                        field_list.append('{0} = db.Column(db.String(255), nullable=True)'.format(field['column_name']))
                if field['data_type'] == 'TEXT':
                    if not field['is_null']:
                        field_list.append('{0} = db.Column(db.TEXT)'.format(field['column_name']))
                    else:
                        field_list.append('{0} = db.Column(db.TEXT, nullable=True)'.format(field['column_name']))
                if field['data_type'] == 'BOOLEAN':
                    if not field['default']:
                        field_list.append('{0} = db.Column(db.Boolean, default=False)'.format(field['column_name']))
                    else:
                        field_list.append('{0} = db.Column(db.Boolean, default=True)'.format(field['column_name']))
                if field['data_type'] == 'JSON':
                    if not field['is_null']:
                        field_list.append('{0} = db.Column(db.JSON)'.format(field['column_name']))
                    else:
                        field_list.append('{0} = db.Column(db.JSON, nullable=True)'.format(field['column_name']))
                if field['data_type'] == 'TIMESTAMP':
                    if not field['is_null']:
                        if not field['on_update_default']:
                            field_list.append('{0} = db.Column(db.DateTime, default=db.func.current_timestamp())'
                                              .format(field['column_name']))
                        else:
                            field_list.append('{0} = db.Column(db.DateTime, default=db.func.current_timestamp(), '
                                              'onupdate=db.func.current_timestamp())'.format(field['column_name']))
                    else:
                        field_list.append('{0} = db.Column(db.DateTime, nullable=True)'.format(field['column_name']))

        join_fields = ";".join(field_list)
        model_fields = join_fields.replace(";", "\n\t")
        return model_fields

    @classmethod
    def get_init_field_string(cls, data):
        field_list = []
        for field in data['fields']:
            field_list.append('self.{field_name} = {field_name}'.format(field_name=field['column_name']))
        join_fields = ";".join(field_list)
        repr_fields = join_fields.replace(";", "\n\t\t")
        return repr_fields

    @classmethod
    def get_init_string(cls, data):
        field_names = cls.get_fields_names(data)
        init_fields = cls.get_init_field_string(data)
        return 'def __init__(self, {field_names}):\n\t\t{init_fields}'.format(field_names=field_names,
                                                                              init_fields=init_fields)

    @staticmethod
    def get_repr_string():
        return 'def __repr__(self):\n\t\treturn "%s(%s)" % (self.__class__.__name__, self.id)'

    @classmethod
    def get_all_method(cls):
        pass

    @classmethod
    def get_by_id_method(cls):
        return "@classmethod" \
               "def get_article_by_id(cls, id):"\
               "\treturn cls.query.filter_by(id=id).first()"

    @classmethod
    def model_string(cls, fields, model, table, data):
        return "from app import db\n" \
               "from app.core.models import Base\n" \
               "\n\nclass {model_name}(Base):\n\t" \
               "__tablename__ = '{table_name}'\n\n\t" \
               "{fields}\n\n\t" \
               "{init_string}\n\n\t" \
               "{repr_string}".\
            format(model_name=model, fields=fields, table_name=table, init_string=cls.get_init_string(data),
                   repr_string=cls.get_repr_string())


def create_model(data, file_path):
    with open(file_path, 'w') as f:
        model_fields = ModelCreator.get_model_fields(data)
        model = data['content_name'].capitalize()
        table = data['content_name'].lower()
        output = ModelCreator.model_string(model_fields, model, table, data)
        f.write(textwrap.dedent(output))

def make_file(data):
    model_package = data['content_name'].lower()
    file_dir = '{}/app/{}/'.format(working_dir, model_package)
    file_path = '{}/app/{}/{}'.format(working_dir, model_package, 'models.py')

    try:
        os.mkdir(file_dir)
    except OSError:
        print("Creation of the directory %s failed" % file_dir)
    else:
        print("Successfully created the directory %s" % file_dir)

    create_model(data, file_path)
    print('Execution completed.')