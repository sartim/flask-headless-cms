import os

working_dir = os.getcwd()


def create_model(data, file_path):
    with open(file_path, 'w') as f:
        for key in data:
            print(key)


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