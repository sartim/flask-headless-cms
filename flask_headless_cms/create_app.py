# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import sys
import os
import argparse
import subprocess
import shutil
import jinja2
import codecs
from whaaaaat import prompt, print_json

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
    args = parser.parse_args()
    return args


def main(args, answers):
    print("\nScaffolding...")

    # Variables #

    appname = args.appname
    fullpath = os.path.join(cwd, appname)
    skeleton_dir = 'skeleton'

    # Tasks #

    # Copy files and folders
    print("Copying files and folders...")
    shutil.copytree(os.path.join(script_dir, skeleton_dir), fullpath)

    # Create config.py
    print("Creating the config...")
    secret_key = codecs.encode(os.urandom(32), 'hex').decode('utf-8')
    basic_auth_password = codecs.encode(os.urandom(32), 'hex').decode('utf-8')
    template = template_env.get_template('.env.jinja2')
    template_var = dict(secret_key=secret_key, db_name=answers['database_name'], db_host=answers['database_host'],
                        db_user=answers['database_user'], db_port=answers['database_port'],
                        basic_auth_user=answers['basic_auth_user'],
                        basic_auth_password=answers['basic_auth_password'] if answers[
                            'basic_auth_password'] else basic_auth_password,
                        is_dev='TRUE' if answers['environment'] == 'Development' else 'FALSE',
                        is_test='TRUE' if answers['environment'] == 'Testing' else 'FALSE',
                        is_prod='TRUE' if answers['environment'] == 'Production' else 'FALSE')
    with open(os.path.join(fullpath,'.env'), 'w') as fd:
        fd.write(template.render(template_var))

    # Git init
    if answers['has_git']:
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
                questions = [
                    {
                        'type': 'confirm',
                        'name': 'has_git',
                        'message': 'Enable Git?'
                    },
                    {
                        'type': 'rawlist',
                        'name': 'environment',
                        'message': 'Environment',
                        'choices': ['Development', 'Testing', 'Testing', 'Production']
                    },
                    {
                        'type': 'rawlist',
                        'name': 'database',
                        'message': 'Please select one of the database engines',
                        'choices': ['PostgreSQL', 'MySQL']
                    },
                    {
                        'type': 'input',
                        'name': 'database_host',
                        'message': 'Please enter your database host',
                    },
                    {
                        'type': 'input',
                        'name': 'database_port',
                        'message': 'Please enter your database port',
                    },
                    {
                        'type': 'input',
                        'name': 'database_name',
                        'message': 'Please enter your database name',
                    },
                    {
                        'type': 'input',
                        'name': 'database_user',
                        'message': 'Please enter your database user',
                    },
                    {
                        'type': 'password',
                        'name': 'password',
                        'message': 'Please enter your database password'
                    },
                    {
                        'type': 'input',
                        'name': 'basic_auth_user',
                        'message': 'Please enter your basic auth user',
                    },
                    {
                        'type': 'password',
                        'name': 'basic_auth_password',
                        'message': 'Please enter your basic auth password'
                    }
                ]
                answers = prompt(questions)
                print_json(answers)
                confirm_question = [
                    {
                        'type': 'confirm',
                        'name': 'confirm_config',
                        'message': 'Do you confirm all the configurations?'
                    }
                ]
                confirm_answer = prompt(confirm_question)
                if confirm_answer['confirm_config']:
                    main(arguments, answers)
                    print("Done!")
                print("Goodbye!")
                break
            else:
                print("Goodbye!")
                break
        else:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').")
            proceed = input("\nProceed (yes/no)? ")