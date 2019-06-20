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
if not os.path.exists(os.path.dirname(bashrc)):
    with open(bashrc, "w") as f:
        pass


def appendToBashrc():
  with open(bashrc, 'r') as f:
    lines = f.readlines()
    for line in lines:
      if pattern.match(line):
        return
    out = open(bashrc, 'a')
    out.write('\n%s' % alias)
    out.close()
    cmd = 'source {}'.format(bashrc)
    os.system(cmd)


class PostDevelopCommand(develop):
    def run(self):
        develop.run(self)
        appendToBashrc()


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        appendToBashrc()


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='flask_headless_cms',
      version='0.0.1',
      description='Flask Headless CMS',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/sartim/flask-headless-cms',
      author='sartim',
      author_email='sarrtim@gmail.com',
      license='MIT',
      packages=find_packages(),
      package_data={'flask_headless_cms': ['templates/*']},
      include_package_data=True,
      install_requires=[
          'requests',
          'Flask',
          'Flask-Cors',
          'Flask-Migrate',
          'Flask-Script',
          'Flask-SQLAlchemy',
          'gevent',
          'gunicorn',
          'psycopg2',
          'psycopg2-binary',
          'whaaaaat',
          'prompt-toolkit==1.0.14',
          'bcrypt',
          'sqlalchemy-utils'
      ],
      cmdclass={
          'develop': PostDevelopCommand,
          'install': PostInstallCommand,
      },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ])
