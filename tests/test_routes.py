def test_home_page(client):
    """GIVEN a Flask application, check the home page response."""
    response = client.get('/')
    assert response.status_code == 200
