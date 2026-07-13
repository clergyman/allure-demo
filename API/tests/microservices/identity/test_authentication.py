def test_login_returns_token_for_valid_user(identity_client):
    response = identity_client.login("buyer@example.com", "correct-password")

    assert response["status_code"] == 200
    assert response["json"]["token"] == "demo-token"


def test_login_rejects_wrong_password(identity_client):
    response = identity_client.login("buyer@example.com", "wrong-password")

    assert response["status_code"] == 401
    assert response["json"]["error"] == "Invalid credentials"

