import json
from project import db
from project.api.models import User


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


def test_add_user(test_client):
    response = test_client.post(
        "/users",
        data=json.dumps({"username": "apatel", "email": "apatel@example.org"}),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())
    print(data["message"])
    assert response.status_code == 201
    assert "apatel@example.org was added!" in data["message"]
    assert data["status"] == "success"


def test_add_user_invalid_json(test_client):
    response = test_client.post(
        "/users",
        data=json.dumps({}),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "Invalid payload." in data["message"]
    assert data["status"] == "fail"


def test_add_user_invalid_json_keys(test_client):
    response = test_client.post(
        "/users",
        data=json.dumps({"email": "apatel@example.org"}),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "Invalid payload." in data["message"]
    assert data["status"] == "fail"


def test_add_user_duplicate_email(test_client):
    test_client.post(
        "/users",
        data=json.dumps({"username": "apatel", "email": "apatel@example.org"}),
        content_type="application/json",
    )

    response = test_client.post(
        "/users",
        data=json.dumps({"username": "apatel", "email": "apatel@example.org"}),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "Sorry. That email already exists." in data["message"]
    assert data["status"] == "fail"


def test_single_user(test_client):
    """Ensure get single user behaves correctly."""
    user = User(username="aditya", email="apatel@example.org")
    db.session.add(user)
    db.session.commit()
    response = test_client.get(f"/users/{user.id}")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert "aditya" in data["data"]["username"]
    assert "apatel@example.org" in data["data"]["email"]
    assert "success" in data["status"]


def test_main_no_users(test_client):
    """Ensure the main route behaves correctly when no users have been
    added to the database."""
    response = test_client.get("/")
    data = response.data.decode()
    assert response.status_code == 200
    assert "All Users" in data
    assert "<p>No users!</p>" in data


def test_main_with_users(test_client):
    """Ensure the main route behaves correctly when users have been added to the database."""

    add_user("aditya", "aditya@notreal.org")
    add_user("patel", "patel@notreal.com")
    response = test_client.get("/")
    data = response.data.decode()

    assert response.status_code == 200
    assert "All Users" in data
    assert "<p>No users!</p>" not in data
    assert "aditya" in data
    assert "patel" in data


def test_main_add_user(test_client):
    """Ensure a new user can be added to the database."""

    response = test_client.post("/", data=dict(username="aditya", email="aditya@sonotreal.com"), follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert "All Users" in data
    assert "<p>No users!</p>" not in data
    assert "aditya" in data
