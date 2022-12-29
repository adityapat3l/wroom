import json

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