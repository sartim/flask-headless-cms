import os

class BaseConfig(object):
    """
    Callable Base Config which takes an object
    """
    # Define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # 50 items per page
    PER_PAGE = 50

    # SQLite for this example
    # Define the database - we are working with
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{host}:{port}/{db}'. \
        format(user=os.environ.get('DB_USERNAME'), pw=os.environ.get('DB_PASSWORD'), host=os.environ.get('DB_HOST'),
               port=os.environ.get('DB_PORT'), db=os.environ.get('DB_NAME'))

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Enable protection against *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for signing the data.
    CSRF_SESSION_KEY = os.environ.get('CSRF_SESSION_KEY')
    # Secret key
    SECRET_KEY = os.environ.get('SECRET_KEY')

    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')


class DevelopmentConfig(BaseConfig):
    """
    Development config which inherits from BaseConfig
    """
    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    Production config which inherits from BaseConfig
    """
    DEBUG = False
    # Sentry config
    SENTRY_CONFIG = {
        'dsn': 'https://28fe6de596ef4d16b56bf7a6c26da6df:c66ce20b345849738f14947729941d80@sentry.io/1274298',
        'include_paths': ['app'],
        'release': '1.0.0'
    }


class TestingConfig(BaseConfig):
    """
    Testing config which inherits from BaseConfig
    """
    DEBUG = False
