import allure


@allure.epic("Demo Shop API")
@allure.feature("Identity Service")
@allure.story("Authentication")
@allure.severity(allure.severity_level.BLOCKER)
@allure.label("layer", "api")
@allure.label("component", "identity-service")
def test_login_returns_token_for_valid_user(identity_client):
    with allure.step("Submit valid buyer credentials"):
        response = identity_client.login("buyer@example.com", "correct-password")

    with allure.step("Verify the identity service returns an access token"):
        assert response["status_code"] == 200
        assert response["json"]["token"] == "demo-token"


@allure.epic("Demo Shop API")
@allure.feature("Identity Service")
@allure.story("Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("layer", "api")
@allure.label("component", "identity-service")
def test_login_rejects_wrong_password(identity_client):
    with allure.step("Submit buyer credentials with the wrong password"):
        response = identity_client.login("buyer@example.com", "wrong-password")

    with allure.step("Verify the identity service rejects the login"):
        assert response["status_code"] == 401
        assert response["json"]["error"] == "Invalid credentials"
