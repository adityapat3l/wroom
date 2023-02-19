# import unittest


from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User
import pytest
import coverage


COV = coverage.coverage(
    branch=True,
    include="project/*",
    omit=[
        "project/tests/*",
        "project/config.py",
    ],
)
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Runs the tests."""
    pytest.main(["-s", "project/tests"])


@cli.command()
def seed_db():
    """Seeds the database."""
    db.session.add(User(username="apatel", email="apatel@example.com"))
    db.session.add(User(username="apatel1", email="apatel1@example.org"))
    db.session.commit()


@cli.command()
def cov():
    pytest.main(["-s", "project/tests"])

    COV.stop()
    COV.save()
    print("Coverage Summary:")
    COV.report()
    COV.html_report()
    COV.erase()


if __name__ == "__main__":
    cli()
