from ennoia import create_app

def test_config():
    # when not testing, no error
    assert not create_app().testing
    # when testing, no error
    assert create_app({'TESTING': True}).testing