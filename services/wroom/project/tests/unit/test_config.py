import os
from flask import current_app

# from project import create_app


def test_app_is_development(development_app):
    assert development_app.config["SECRET_KEY"] == "my_precious"
    assert current_app is not None
    assert development_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
    assert development_app.config['DEBUG_TB_ENABLED']


def test_app_is_testing(testing_app):
    assert testing_app.config["SECRET_KEY"] == "my_precious"
    assert testing_app.config["TESTING"]
    assert testing_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_TEST_URL")
    assert testing_app.config['DEBUG_TB_ENABLED']


def test_app_is_production(production_app):
    assert production_app.config["SECRET_KEY"] == "my_precious"
    assert not production_app.config["TESTING"]
    assert not production_app.config['DEBUG_TB_ENABLED']
