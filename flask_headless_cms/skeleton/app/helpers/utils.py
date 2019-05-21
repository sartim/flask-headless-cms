import os

working_dir = os.getcwd()


def create_dir(dir):
    try:
        os.mkdir(dir)
    except OSError:
        print("Creation of the directory %s failed" % dir)
    else:
        print("Successfully created the directory %s" % dir)
        return True
    return False
