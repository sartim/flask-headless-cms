### Features

- Support SQLAlchemy models
- Model generator
- Databases: PostgreSQL

# Flask Headless CMS

[![Open Source Love](https://img.shields.io/badge/language-python-green.svg)](https://github.com/sartim/flask-headless-cms)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/sartim/flask-headless-cms)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/sartim/flask-headless-cms/blob/master/LICENSE)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/sartim/flask-headless-cms/issues)

### Setup
_On Mac_

* Install [Homebrew](https://docs.brew.sh/Installation)
* Use the following command to install Python 3.x via Homebrew

    
    $ brew install python
    $ pip3 install virtualenv

_On Linux_
   
    $ pip3 install virtualenv

#### Create alias

    $ python
    
        >>> import os
        >>> import flask_headless_cms
        >>> os.path.dir_name(flask_headless_cms.__file__)
        '/path/to/flask_headless_cms'
        
    $ alias flaskcli="python /path/to/flask_headless_cms/create_app.py"
    $ flaskcli <new_project> -s skeleton -g
    $ cd <new_project>

#### Make Migrations
    
    $ python manage.py db init
    $ python manage.py db migrate
    $ python manage.py db upgrade
 