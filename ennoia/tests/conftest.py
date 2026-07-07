"""
Configures the tests

"""
import os
import tempfile
import pytest

from ennoia import create_app
from ennoia.db import get_db, init_db

# to read the test data
with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
   data = f.read().decode('utf8')

@pytest.fixture
def app():
    # not exactly sure why this is needed
    form_data, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })
    
    # what exactly is app context?
    with app.app_context():
        init_db()
        get_db.executescript(data)

    # does 'yield' store a response so that it can get later accessed?
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()