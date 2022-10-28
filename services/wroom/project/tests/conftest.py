from project import app
from project import db as _db
import pytest


@pytest.fixture()
def testing_app():

    app.config.from_object('project.config.TestingConfig')
    yield app


@pytest.fixture(scope='session')
def db(testing_app):
    with app.app_context():
        _db.create_all()
        _db.session.commit()
        yield _db
        _db.session.remove()
        _db.drop_all()


@pytest.fixture()
def development_app():
    app.config.from_object('project.config.DevelopmentConfig')
    return app


@pytest.fixture()
def production_app():
    app.config.from_object('project.config.ProductionConfig')
    return app


@pytest.fixture()
def test_client(testing_app):
    return app.test_client()

