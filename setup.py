from setuptools import setup

setup(name='FlaskHeadlessCms',
      version='0.1',
      description='Flask Headless CMS',
      url='https://github.com/sartim/flask-headless-cms',
      author='sartim',
      author_email='sarrtim@gmail.com',
      license='MIT',
      packages=['flask_headless_cms'],
      install_requires=[
          'requests',
          'Flask',
          'Flask-Bcrypt',
          'Flask-Cors',
          'Flask-Migrate',
          'Flask-Script',
          'Flask-SQLAlchemy',
          'gevent',
          'greenlet',
          'gunicorn',
          'psycopg2',
          'inquirer'
      ],
      dependency_links=['https://github.com/sartim/flask-headless-cms/master#egg=package-1.0'],
      zip_safe=False)