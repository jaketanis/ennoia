"""
Ennoia

"""
import os
from flask import Flask

def create_app(test_config=None):
    # to start the app in the current python file and use the instance folder for configurations
    ennoia = Flask(__name__, instance_relative_config=True)

    """ 
    configurations
    
    """
    ennoia.config.from_mapping(
        #sets the secret_key to dev if there is not a secret key in config.
        SECRET_KEY=os.environ.get('SECRET_KEY','dev'),
        #stores the database in the instance folder
        DATABASE=os.path.join(ennoia.instance_path, 'ennoia.sqlite'),
    )

    #if test_config is None:
        # if testing, the tests from config.py are used
    #    ennoia.config.from_pyfile('config.py', silent=True)
    #else:
        #configurations for testing if test_config is true
    #    ennoia.config.update(test_config)

    #makes the instance folder if not present.
    #needed because Flask does not make one automatically.
    
    try:
        os.makedirs(ennoia.instance_path)
    except OSError:
        pass

    """
    database connections and blueprints

    """
    #to initialize the databasea
    from . import db
    db.init_app(ennoia)

   # to initialize the schema
    from . import schema
    schema.init_app(ennoia)

    # to register the blueprints
    from . import auth
    from . import books
    from . import api
    ennoia.register_blueprint(auth.bp)
    ennoia.register_blueprint(books.bp)
    ennoia.register_blueprint(api.bp)
    
    #index route
    ennoia.add_url_rule('/', endpoint='index')

    
    return ennoia
