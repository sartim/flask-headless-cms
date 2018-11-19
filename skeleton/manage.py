"""
This handles management commands for app
"""
import logging

import sys
from flask_migrate import MigrateCommand, Migrate
from flask_script import Server, Manager, prompt_bool, Shell, prompt_pass, prompt
from skeleton.app import controllers
from skeleton.app import User
from skeleton.app import validator
from skeleton.app import *
from skeleton.app import models


def _make_context():
    return dict(app=app, db=db, models=models)


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("runserver", Server(port=5000, use_reloader=True))
manager.add_command('db', MigrateCommand)
manager.add_command("shell", Shell(make_context=_make_context))


@manager.command
def create(default_data=True, sample_data=False):
    """
    Creates database tables from sqlalchemy models
    :param default_data:
    :param sample_data:
    """
    db.create_all()
    sys.stdout.write("Finished creating tables!!! \n")


# DO NOT ever run this on production server
@manager.command
def drop():
    """Drops database tables"""""
    if prompt_bool("Are you sure you want to drop all tables?"):
        db.drop_all()
        sys.stdout.write("Finished dropping tables!!! \n")


# DO NOT ever run this on production server
# Also never run it twice
@manager.command
def recreate(default_data=True, sample_data=False):
    """
    Recreates database tables (same as issuing 'drop' and then 'create')
    :param default_data:
    :param sample_data: received
    """
    drop()
    create(default_data, sample_data)


@manager.command
def create_article_data():
    print("Please wait as the data is inserted..")
    controllers.article_scroll()
    print("Finished creating data!!!")


@manager.command
def createsuperuser():
    """Creates the superuser"""

    first_name = prompt("First name")
    last_name = prompt("Last name")
    email = prompt("Email")
    validate_email = validator.email_validator(email)
    password = prompt_pass("Password")
    confirm_password = prompt_pass("Confirm Password")
    validate_pwd = validator.password_validator(password)

    if not validate_email:
        sys.stdout.write("Not a valid email \n")

    if validate_pwd:
        sys.stdout.write("Not a valid password \n")

    if not validate_pwd:
        if not validate_pwd == confirm_password:
            sys.stdout.write("Passwords do not match \n")

    if validate_email and not validate_pwd:
        try:
            user = User(first_name=first_name, last_name=last_name, email=email, password=password, is_super_user=True,
                        is_active=True)
            db.session.add(user)
            db.session.commit()
            sys.stdout.write("Successfully created admin account \n")
        except Exception as e:
            sys.stdout.write(str(e))


@manager.command
def createadmin():
    """Creates the admin user"""

    first_name = prompt("First name")
    last_name = prompt("Last name")
    email = prompt("Email")
    validate_email = validator.email_validator(email)
    password = prompt_pass("Password")
    confirm_password = prompt_pass("Confirm Password")
    validate_pwd = validator.password_validator(password)

    if not validate_email:
        sys.stdout.write("Not a valid email \n")

    if validate_pwd:
        sys.stdout.write("Not a valid password \n")

    if not validate_pwd:
        if not validate_pwd == confirm_password:
            sys.stdout.write("Passwords do not match \n")

    if validate_email and not validate_pwd:
        try:
            user = User(first_name=first_name, last_name=last_name, email=email, password=password, is_admin=True,
                        is_active=True)
            db.session.add(user)
            db.session.commit()

            sys.stdout.write("Successfully created admin account \n")
        except Exception as e:
            sys.stdout.write(str(e))


if __name__ == '__main__':
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s %(message)s - {%(pathname)s:%(lineno)d}")
    handler = logging.FileHandler('./logs/server.log')
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    manager.run()
