def test_register_page(client):
    response = client.get('/auth/register')
    assert response.status_code == 200


def test_login_page(client):
    response = client.get('/auth/login')
    assert response.status_code == 200


def test_login_process(client):
    # Pehle test user banana parta hai
    from models import User
    from extensions import db

    user = User(username="testuser", email="test@example.com")
    user.set_password("password123")

    with client.application.app_context():
        db.session.add(user)
        db.session.commit()

    # Ab login karte hain
    response = client.post('/auth/login', data={
        "username": "testuser",
        "password": "password123"
    }, follow_redirects=True)

    assert b"Dashboard" in response.data
