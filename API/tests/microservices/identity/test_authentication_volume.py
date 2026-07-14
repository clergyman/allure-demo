import allure
import pytest

from flaky import maybe_fail


LOGIN_CASES = [
    *[
        (f"unknown-buyer-{index}", f"buyer-{index}@example.com", "correct-password", 401)
        for index in range(17)
    ],
    *[
        (f"known-buyer-{index}", "buyer@example.com", "correct-password", 200)
        for index in range(7)
    ],
    *[
        (f"bad-password-{index}", "buyer@example.com", f"wrong-password-{index}", 401)
        for index in range(9)
    ],
]


@allure.epic("Demo Shop API")
@allure.feature("Identity Service")
@allure.story("Authentication volume")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("layer", "api")
@allure.label("component", "identity-service")
@pytest.mark.parametrize(
    ("case_id", "email", "password", "expected_status"), LOGIN_CASES
)
def test_identity_login_volume(
    identity_client, case_id, email, password, expected_status
):
    with allure.step("Simulate identity service stability"):
        maybe_fail(0, "identity session cache timed out")

    with allure.step(f"Submit login request for {email} ({case_id})"):
        response = identity_client.login(email, password)

    with allure.step("Verify login response status"):
        assert response["status_code"] == expected_status
