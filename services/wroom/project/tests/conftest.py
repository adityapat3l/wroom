from project import create_app
from project import db as _db
import pytest

app = create_app()

@pytest.fixture()
def testing_app():

    app.config.from_object('project.config.TestingConfig')
    
    with app.app_context():
        _db.create_all()
        _db.session.commit()
        yield app
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
    return testing_app.test_client()


@pytest.fixture()
def test_users(testing_app):
    return testing_app.test_client()


