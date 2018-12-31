from setuptools import setup, find_packages

NAME = 'FlaskHeadlessCms'

setup(name=NAME,
      version='0.1',
      description='Flask Headless CMS',
      url='https://github.com/sartim/flask-headless-cms',
      author='sartim',
      author_email='sarrtim@gmail.com',
      license='MIT',
      packages=find_packages(),
      package_data={'flask_headless_cms': ['templates/.env.jinja2']},
      include_package_data=True,
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
          'psycopg2-binary',
          'whaaaaat',
          'prompt-toolkit==1.0.14'
      ])