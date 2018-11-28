import os
import textwrap

working_dir = os.getcwd()

class ModelCreator:

    @staticmethod
    def obj_repr_string():
        return 'def __init__(self, name):\n\t\tself.id = id'

    @staticmethod
    def init_string():
        return 'def __repr__(self):\n\t\treturn "%s(%s)" % (self.__class__.__name__, self.id)'

    @classmethod
    def model_string(cls, fields, tbl_name):
        return "from app import db\n" \
               "\n\nclass {model_name}(Base):\n\t" \
               "__tablename__ = '{table_name}'\n\n\t" \
               "{fields}\n\n\t" \
               "{init_string}\n\n\t" \
               "{repr_string}".\
            format(model_name='AccountUser', fields=fields, table_name=tbl_name, init_string=cls.init_string(),
                   repr_string=cls.obj_repr_string())


def create_model(data, file_path):
    with open(file_path, 'w') as f:
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


        join_fields = ";".join(field_list)
        fields = join_fields.replace(";", "\n\t")

        output = ModelCreator.model_string(fields, data['table'])
        print(output)
        f.write(textwrap.dedent(output))

def make_file(data):
    file_dir = '{}/app/{}/'.format(working_dir, data['dir'])
    file_path = '{}/app/{}/{}'.format(working_dir, data['dir'], 'models.py')

    try:
        os.mkdir(file_dir)
    except OSError:
        print("Creation of the directory %s failed" % file_dir)
    else:
        print("Successfully created the directory %s" % file_dir)

    create_model(data, file_path)
    print('Execution completed.')