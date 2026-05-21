"""
Ennoia

"""
import os
from flask import Flask

def create_app(test_config=None):
    # to start the app in the current python file and use the instance folder for configurations
    bookshelf = Flask(__name__, instance_relative_config=True)

    """ 
    configurations
    
    """
    bookshelf.config.from_mapping(
        #for development only, need to change for production
        SECRET_KEY=os.environ.get('SECRET_KEY','dev'),
        #stores the database in the instance folder
        DATABASE=os.path.join(bookshelf.instance_path, 'bookshelf.sqlite'),
    )

    if test_config is None:
        # if testing, the tests from config.py are used
        bookshelf.config.from_pyfile('config.py', silent=True)
    else:
        #configurations for testing if test_config is true
        bookshelf.config.update(test_config)

    #makes the instance folder if not present.
    #needed because Flask does not make one automatically.
    try:
        os.makedirs(bookshelf.instance_path)
    except OSError:
        pass

    """
    database connections and blueprints

    """
    #to initialize the database
    from . import db
    db.init_app(bookshelf)

   # to initialize the schema
    from . import schema
    schema.init_app(bookshelf)

    # to register the blueprints
    from . import auth
    from . import books
    from . import api
    bookshelf.register_blueprint(auth.bp)
    bookshelf.register_blueprint(books.bp)
    bookshelf.register_blueprint(api.bp)
    
    #index route
    bookshelf.add_url_rule('/', endpoint='index')

    
    return bookshelf
