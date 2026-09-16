import allure

from flaky import maybe_fail


@allure.epic("Demo Shop")
@allure.feature("Identity")
@allure.story("Authentication volume")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "identity-service")
def test_identity_login_returns_token_for_known_buyer(identity_client):
    with allure.step("Simulate identity service stability"):
        maybe_fail(0, "identity session cache timed out")

    with allure.step("Submit login request for a known buyer"):
        response = identity_client.login("buyer@example.com", "correct-password")

    with allure.step("Verify access token and user identity are returned"):
        assert response["status_code"] == 200
        assert response["json"]["token"] == "demo-token"
        assert response["json"]["user"]["id"] == "user-1"


@allure.epic("Demo Shop")
@allure.feature("Identity")
@allure.story("Authentication volume")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "identity-service")
def test_identity_login_rejects_unknown_buyer(identity_client):
    with allure.step("Submit login request for an unknown buyer"):
        response = identity_client.login("buyer-17@example.com", "correct-password")

    with allure.step("Verify unknown account cannot authenticate"):
        assert response["status_code"] == 401
        assert response["json"]["error"] == "Invalid credentials"


@allure.epic("Demo Shop")
@allure.feature("Identity")
@allure.story("Authentication volume")
@allure.severity("critical")
@allure.label("layer", "api")
@allure.label("component", "identity-service")
def test_identity_login_rejects_bad_password_for_known_buyer(identity_client):
    with allure.step("Submit login request with a bad password"):
        response = identity_client.login("buyer@example.com", "wrong-password-9")

    with allure.step("Verify known account is protected by password check"):
        assert response["status_code"] == 401
        assert response["json"]["error"] == "Invalid credentials"
