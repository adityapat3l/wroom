import os
from flask import current_app
from project import app


def test_app_is_development(development_app):
    assert development_app.config['SECRET_KEY'] == 'my_precious'
    assert current_app is not None
    assert development_app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_URL')


def test_app_is_testing(testing_app):
    assert app.config['SECRET_KEY'] == 'my_precious'
    assert app.config['TESTING']
    assert not app.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_TEST_URL')


def test_app_is_production(production_app):
    assert app.config['SECRET_KEY'] == 'my_precious'
    assert not app.config['TESTING']
