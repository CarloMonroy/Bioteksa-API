from server import app

def test_endpoint_post():
    """
    Tests our post endpoint
    """

    with app.test_client() as test_client:
        post_response = test_client.post('/cultivos')
        assert post_response.status_code == 405

def test_endpoint_get():
    """
    Tests our get endpoint
    """

    with app.test_client() as test_client:
        get_response = test_client.get('/cultivos?user_id=2')
        assert get_response.status_code == 200

def test_endpoint_not_found():
    """
    Tests not found url
    """

    with app.test_client() as test_client:
        get_response = test_client.get('/randomurl')
        assert get_response.status_code == 404