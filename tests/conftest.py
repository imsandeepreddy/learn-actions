import pytest
from app import app as flask_app # Import your app instance directly

@pytest.fixture()
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture()
def client(app):
    return app.test_client()
