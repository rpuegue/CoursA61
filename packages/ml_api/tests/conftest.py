import pytest

import sys
sys.path.append("./")

#from api.app import create_app
#from api.config import TestingConfig
import api.app as ap
import api.config as ac
@pytest.fixture
def app():
    app = ap.create_app(config_object=ac.TestingConfig)

    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client
        
