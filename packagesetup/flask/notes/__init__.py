# The __init__.py files are required to make Python treat directories 
# containing the file as packages. This prevents directories with a common name, 
# such as string , unintentionally hiding valid modules that occur later 
# on the module search path.

import os

from flask import Flask

def create_app(test_config=None): #Use "None" to add in own config for automated testing
    app = Flask(__name__)  #Flask instance of the name of current module.
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev')
    )
    if test_config is None:  # If test config exists or not.
        app.config.from_pyfile('comfig.py', silent=True) #Load more configs from a different python file.  Silent=True makes it still exicute if the file doesn't exist.
    else:
        app.config.from_mapping(test_config)  # see above

    return app
