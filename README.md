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

    $ brew install python
    $ pip3 install virtualenv

_On Linux_
   
    $ pip3 install virtualenv
    
### Installation
    
    $ pip3 install FlaskHeadlessCms
    
or 

    $ git clone https://github.com/sartim/flask-headless-cms.git
    $ cd flask-headless-cms
    $ python install .

After installation close & start a new terminal session.

### Start new project

    $ flaskcli <new_project>
    
#### Make Migrations
    
    $ cd <new_project>
    $ python manage.py db init
    $ python manage.py db migrate
    $ python manage.py db upgrade
 
 
### API 

URL: `/field/param`

METHOD: `POST`

BODY:
 
```
{
    "dir": "package_name",
    "model": "ModelName",
    "table": "table_name",
    "fields": [{
            "column_name": "id",
            "data_type": "data_type",
            "data_size": <integer>,
            "is_primary_key": boolean,
            "is_foreign_key": boolean,
            "is_null": boolean,
            "default": null
	    },
	    ............
	]
}
```

_Example_ 

```
{
    "dir": "account",
    "model": "AccountUser",
    "table": "account_users",
    "fields": [
    	{
	    	"column_name": "id",
	    	"data_type": "INTEGER",
	    	"data_size": null,
	    	"is_primary_key": true,
	    	"is_foreign_key": true,
			"is_null": false,
			"default": null
	     },
	     {
	    	"column_name": "name",
	    	"data_type": "VARCHAR",
	    	"data_size": 255,
	    	"is_primary_key": false,
	    	"is_foreign_key": false,
	    	"is_null": false,
	    	"default": null
	     },
	     {
	         "column_name": "password",
	         "data_type": "VARCHAR",
	         "data_size": 255,
	         "is_primary_key": false,
	         "is_foreign_key": false,
	         "is_null": false,
	         "defualt": null
	     },
	     {
	         "column_name": "phone_number",
	         "data_type": "VARCHAR",
	         "data_size": 255,
	         "is_primary_key": false,
	         "is_foreign_key": false,
	         "is_null": false,
	         "default": null
	     },
	     {
	         "column_name": "is_active",
	         "data_type": "BOOLEAN",
	         "data_size": null,
	         "is_primary_key": false,
	         "is_foreign_key": false,
	         "is_null": false,
	         "default": false
	     }
	]
}
```