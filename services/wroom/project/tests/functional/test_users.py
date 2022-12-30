import json
from project import db
from project.api.models import User

def test_add_user(test_client):
    response = test_client.post('/users',
                    data=json.dumps({
                        'username': 'apatel',
                        'email': 'apatel@example.org'
                        }),
                        content_type='application/json',
                        )
    data = json.loads(response.data.decode())
    print(data['message'])
    assert response.status_code == 201
    assert 'apatel@example.org was added!'in data['message']
    assert data['status'] == 'success'
    
    
def test_add_user_invalid_json(test_client):
    response = test_client.post(
                                '/users',
                                data=json.dumps({}),
                                content_type='application/json',
                                )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert 'Invalid payload.' in data['message']
    assert data['status'] == 'fail'
    
    
    
def test_add_user_invalid_json_keys(test_client):
    response = test_client.post(
                        '/users',
                        data=json.dumps({'email': 'apatel@example.org'}),
                        content_type='application/json',
                        )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert 'Invalid payload.' in data['message']
    assert data['status'] == 'fail'
    
    
def test_add_user_duplicate_email(test_client):
    test_client.post('/users',
                    data=json.dumps({
                        'username': 'apatel',
                        'email': 'apatel@example.org'
                        }),
                        content_type='application/json',
                        )
    
    response = test_client.post('/users',
                    data=json.dumps({
                        'username': 'apatel',
                        'email': 'apatel@example.org'
                        }),
                        content_type='application/json',
                        )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert 'Sorry. That email already exists.' in data['message']
    assert data['status'] == 'fail'
    
    
def test_single_user(test_client):
    """Ensure get single user behaves correctly."""
    user = User(username='aditya', email='apatel@example.org')
    db.session.add(user)
    db.session.commit()
    response = test_client.get(f'/users/{user.id}')
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert 'aditya' in data['data']['username']
    assert 'apatel@example.org' in data['data']['email']
    assert 'success' in data['status']
    
    
