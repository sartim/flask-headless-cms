import sqlalchemy
from sqlalchemy_utils import database_exists, create_database


def create(**kwargs):
    """
    Create Database
    :return:
    """
    engine = sqlalchemy.create_engine("postgres://{db_user}:{db_password}@{db_host}:{db_port}/postgres"
                                      .format(db_user=kwargs['db_user'],
                                              db_host=kwargs['db_host'],
                                              db_password=kwargs['db_password'],
                                              db_port=kwargs['db_port'],
                                              db_name=kwargs['db_name']))
    conn = engine.connect()
    conn.execute("commit")
    if not database_exists('postgres://postgres@localhost/name'):
        create_database('postgres://postgres@localhost/name')
        return True
    return False
