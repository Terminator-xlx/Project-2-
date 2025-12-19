
import pytest
from app import create_app, db
from app.models import User
from config import TestingConfig
import json
import pytest
from app import create_app
from app import db
from config import TestingConfig


@pytest.fixture
def app():
    """Простая фикстура приложения"""
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Простая фикстура клиента"""
    return app.test_client()