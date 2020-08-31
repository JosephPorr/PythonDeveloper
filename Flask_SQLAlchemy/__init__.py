# To create a package we need to have a directory with our package name 
# that includes a __init__.py.  This is used as a placeholder for
# the src.  The __init__.py files are required to make Python treat the 
# directories as containing packages; this is done to prevent directories 
# with a common name, such as string, from unintentionally hiding valid 
# modules that occur later on the module search path.

import os

from flask import Flask
from flask_migrate import Migrate

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from .models import db

    db.init_app(app)
    migrate = Migrate(app, db)

    return app