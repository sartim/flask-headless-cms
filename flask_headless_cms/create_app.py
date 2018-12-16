# -*- coding: utf-8 -*-

import sys
import os
import argparse
import subprocess
import shutil
import jinja2
import codecs

# Globals #
cwd = os.getcwd()
script_dir = os.path.dirname(os.path.realpath(__file__))

# Jinja2 environment
template_loader = jinja2.FileSystemLoader(
    searchpath=os.path.join(script_dir, "templates"))
template_env = jinja2.Environment(loader=template_loader)


def get_arguments(argv):
    parser = argparse.ArgumentParser(description='Scaffold a Flask CMS Skeleton.')
    parser.add_argument('appname', help='The application name')
    parser.add_argument('-s', '--skeleton', help='The skeleton folder to use.')
    parser.add_argument('-t', '--type', help='The database type to use')
    parser.add_argument('-d', '--databasename', help='The database name to use')
    parser.add_argument('-i', '--databasehost', help='The database host name to use')
    parser.add_argument('-u', '--databaseuser', help='The database user name to use')
    parser.add_argument('-p', '--databaseport', help='The database port to use')
    parser.add_argument('-e', '--env', help='The environment to use')
    parser.add_argument('-g', '--git', action='store_true')
    args = parser.parse_args()
    return args


def main(args):
    print("\nScaffolding...")

    # Variables #

    appname = args.appname
    fullpath = os.path.join(cwd, appname)
    skeleton_dir = args.skeleton
    database_type = args.type
    db_name = args.databasename
    db_host = args.databasehost
    db_user = args.databaseuser
    db_port = args.databaseport
    env = args.env

    # Tasks #

    # Copy files and folders
    print("Copying files and folders...")
    shutil.copytree(os.path.join(script_dir, skeleton_dir), fullpath)

    # Create config.py
    print("Creating the config...")
    secret_key = codecs.encode(os.urandom(32), 'hex').decode('utf-8')
    basic_auth_password = codecs.encode(os.urandom(32), 'hex').decode('utf-8')
    template = template_env.get_template('.env.jinja2')
    template_var = {
        'secret_key': secret_key,
        'db_name': db_name,
        'db_host': db_host,
        'db_user': db_user,
        'db_port': db_port,
        'basic_auth_user': 'app',
        'basic_auth_password': basic_auth_password,
        'is_dev': 'TRUE' if env == 'dev' else 'FALSE',
        'is_test': 'TRUE' if env == 'test' else 'FALSE',
        'is_prod': 'TRUE' if env == 'prod' else 'FALSE'
    }
    with open(os.path.join(fullpath,'.env'), 'w') as fd:
        fd.write(template.render(template_var))

    # Git init
    if args.git:
        print("Initializing Git...")
        output, error = subprocess.Popen(
            ['git', 'init', fullpath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).communicate()
        if error:
            with open('git_error.log', 'w') as fd:
                fd.write(error.decode('utf-8'))
                print("Error with git init")
                sys.exit(2)


if __name__ == '__main__':
    arguments = get_arguments(sys.argv)

    if sys.version_info < (3, 0):
        input = raw_input
    proceed = input("Creating Flask Skeleton\nProceed (yes/no)? ")
    valid = ["yes", "y", "no", "n"]
    while True:
        if proceed.lower() in valid:
            if proceed.lower() == "yes" or proceed.lower() == "y":
                main(arguments)
                print("Done!")
                break
            else:
                print("Goodbye!")
                break
        else:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').")
            proceed = input("\nProceed (yes/no)? ")
