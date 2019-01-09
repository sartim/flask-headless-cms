import sys

from flask_migrate import MigrateCommand, Migrate
from flask_script import Server, Manager, prompt_bool, Shell
from app import db
from app.core import models
from app.root_api import *
from app.generator_api import *


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


if __name__ == '__main__':
    manager.run()
