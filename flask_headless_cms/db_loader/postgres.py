import sqlalchemy


def create(**kwargs):
    """
    Create Database
    :return:
    """
    engine = sqlalchemy.create_engine("postgres://{db_user}@{db_password}/{db_name}"
                                      .format(db_user=kwargs['db_user'],
                                              db_password=kwargs['db_password'],
                                              db_name=kwargs['db_name']))
    conn = engine.connect()
    conn.execute("commit")
    conn.execute("CREATE DATABASE {db_name}".format(db_name=kwargs['db_name']))
    conn.close()
