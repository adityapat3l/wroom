import json
import pytest

def test_add_user(test_client):
    response = test_client.post('/users',
                    data=json.dumps({
                        'username': 'apatel',
                        'email': 'apatel@example.org'
                        }),
                        content_type='application/json',
                        )
    data = json.loads(response.data.decode())
    assert response.status_code == 201
    assert 'apatel@example.org was added!'in data['message']
    assert data['status'] == 'success'