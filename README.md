# Flask Headless CMS

[![Open Source Love](https://img.shields.io/badge/language-python-green.svg)](https://github.com/sartim/flask-headless-cms)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/sartim/flask-headless-cms/blob/master/LICENSE)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/sartim/flask-headless-cms/issues)
[![Build Status](https://travis-ci.com/sartim/flask-headless-cms.svg?branch=master)](https://travis-ci.com/sartim/flask-headless-cms)

## Overview

A tool for generating a database structure and an API for content management. Generated SQLAlchemy models and endpoints based on content types created via API.

### Features

- Support SQLAlchemy models
- Model generator
- Databases: PostgreSQL

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
    "content_name": "<name>",
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
	],
	"methods": ["GET, "POST"]
}
```

_Example_ 

**With no relation**
```
{
    "content_name": "user",
    "fields": [
    	{
	    	"column_name": "id",
	    	"data_type": "INTEGER",
	    	"data_size": null,
	    	"is_primary_key": true,
	    	"is_foreign_key": false,
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
	     },
	     {
	         "column_name": "confirmed_date",
	         "data_type": "TIMESTAMP",
	         "data_size": null,
	         "is_primary_key": false,
	         "is_foreign_key": false,
	         "is_null": false,
	         "default": "CURRENT_TIMESTAMP",
	         "on_update_default": null
	     }
	],
	"methods": ["GET", "POST", "PUT", "DELETE"]
}
```

**With relation**

```
{
    "content_name": "user_role",
    "fields": [
    	{
	    	"column_name": "user_id",
	    	"data_type": "INTEGER",
	    	"is_primary_key": true,
	    	"is_foreign_key": true,
	    	"content_name_relation": "user"
	     },
	     {
	    	"column_name": "role_id",
	    	"data_type": "INTEGER",
	    	"is_primary_key": true,
	    	"is_foreign_key": true,
	    	"content_name_relation": "role"
	     },
	],
	"methods": ["GET", "POST", "PUT", "DELETE"]
}
```

_Overriding house keeping fields_
```
{
    "content_name": "user",
    "fields": [
        .......
        {
             "column_name": "created_date",
             "data_type": "TIMESTAMP",
             "data_size": null,
             "is_primary_key": false,
             "is_foreign_key": false,
             "is_null": false,
             "default": "CURRENT_TIMESTAMP",
             "on_update_default": null
         },
         {
             "column_name": "updated_date",
             "data_type": "TIMESTAMP",
             "data_size": null,
             "is_primary_key": false,
             "is_foreign_key": false,
             "is_null": false,
             "default": "CURRENT_TIMESTAMP",
             "on_update_default": "CURRENT_TIMESTAMP"
         }
         .......
    ]
}
 ```
 
| Allowed Fields        | Type           | Example                                         |
| ----------------      |:-------------: | -----------------------------------------------:|
| column_name           |   String       |   first_name, name, user_id                     |
| data_type             |   String       |   VARCHAR, TIMESTAMP, INTEGER, BOOLEAN, DECIMAL |
| data_size             |   Integer      |   255                                           |
| is_primary_key        |   Boolean      |   true, false                                   |
| is_foreign_key        |   Boolean      |   true, false                                   |
| is_null               |   Boolean      |   true, false                                   |
| default               |   String       |   false, CURRENT_TIMESTAMP                      |
| on_update_default     |   String       |   CURRENT_TIMESTAMP                             |
| content_name_relation |   String       |   <content_name>                                |
