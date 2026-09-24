def test_home_page(client):
    # Must redirect to login because home has @login_required
    response = client.get('/', follow_redirects=True)
    assert b"Login" in response.data


def test_dashboard_requires_login(client):
    response = client.get('/dashboard', follow_redirects=True)
    assert b"Login" in response.data


def test_dashboard_shows_sorted_low_stock_alerts_for_current_user(client, app):
    from extensions import db
    from models import Item, User

    user = User(username="alert-user", email="alert@example.com")
    user.set_password("password123")
    other_user = User(username="other-user", email="other@example.com")
    other_user.set_password("password123")

    with app.app_context():
        db.session.add_all([user, other_user])
        db.session.commit()
        db.session.add_all([
            Item(name="Low quantity", quantity=3, price=10, user_id=user.id),
            Item(name="Out of stock", quantity=0, price=10, user_id=user.id),
            Item(name="Healthy stock", quantity=5, price=10, user_id=user.id),
            Item(name="Someone else's low stock", quantity=1, price=10, user_id=other_user.id),
        ])
        db.session.commit()
        user_id = user.id

    with client.session_transaction() as session:
        session["_user_id"] = str(user_id)
        session["_fresh"] = True
    response = client.get("/dashboard")

    assert response.status_code == 200
    assert b"Low-stock alerts" in response.data
    assert b"Out of stock" in response.data
    assert b"Low quantity" in response.data
    assert b"Someone else's low stock" not in response.data
    assert response.data.index(b"Out of stock") < response.data.index(b"Low quantity")
    assert b"Healthy stock" in response.data


def test_dashboard_uses_configured_low_stock_threshold(client, app):
    from extensions import db
    from models import Item, User

    app.config["LOW_STOCK_THRESHOLD"] = 8
    user = User(username="threshold-user", email="threshold@example.com")
    user.set_password("password123")

    with app.app_context():
        db.session.add(user)
        db.session.commit()
        db.session.add(Item(
            name="Threshold alert",
            quantity=7,
            price=10,
            user_id=user.id,
        ))
        db.session.commit()
        user_id = user.id

    with client.session_transaction() as session:
        session["_user_id"] = str(user_id)
        session["_fresh"] = True
    response = client.get("/dashboard")

    assert b"fewer than 8 units" in response.data
    assert b"Threshold alert" in response.data
