import os
import re

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from distutils.sysconfig import get_python_lib

installed_path = '{path}/{name}'.format(path=get_python_lib(), name='flask_headless_cms')
alias = 'alias flaskcli="python {0}/create_app.py"'.format(installed_path)
pattern = re.compile(alias)
homefolder = os.path.expanduser('~')
bashrc = os.path.abspath('%s/.bashrc' % homefolder)


def appendToBashrc():
  with open(bashrc, 'r') as f:
    lines = f.readlines()
    for line in lines:
      if pattern.match(line):
        return
    out = open(bashrc, 'a')
    out.write('\n%s' % alias)
    out.close()


class PostDevelopCommand(develop):
    def run(self):
        develop.run(self)
        appendToBashrc()


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        appendToBashrc()


setup(name='FlaskHeadlessCms',
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
      ],
      cmdclass={
          'develop': PostDevelopCommand,
          'install': PostInstallCommand,
      })