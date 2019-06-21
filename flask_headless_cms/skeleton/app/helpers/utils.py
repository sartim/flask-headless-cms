import os

working_dir = os.getcwd()


def create_dir(dir):
    try:
        os.mkdir(dir)
        print("Successfully created the directory %s" % dir)
        return True
    except OSError:
        print("Creation of the directory %s failed" % dir)
        return False
