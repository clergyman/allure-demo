import allure
import pytest


def identity_metadata(story: str, severity: str = "normal"):
    allure.dynamic.epic("Demo Shop")
    allure.dynamic.feature("Identity")
    allure.dynamic.story(story)
    allure.dynamic.severity(severity)
    allure.dynamic.label("component", "identity-service")


def verify_login_success(identity_client, email: str = "buyer@example.com"):
    with allure.step(f"Submit successful login for {email}"):
        response = identity_client.login(email, "correct-password")

    with allure.step("Verify authenticated identity payload"):
        assert response["status_code"] == 200
        assert response["json"]["token"] == "demo-token"
        assert response["json"]["user"]["email"] == email
        assert response["json"]["user"]["id"] == "user-1"


def verify_login_rejected(identity_client, email: str, password: str):
    with allure.step(f"Submit rejected login for {email}"):
        response = identity_client.login(email, password)

    with allure.step("Verify authentication is rejected"):
        assert response["status_code"] == 401
        assert response["json"]["error"] == "Invalid credentials"


def test_identity_known_buyer_can_start_session(identity_client):
    identity_metadata("Known buyer session", "blocker")
    verify_login_success(identity_client)


def test_identity_known_buyer_receives_token(identity_client):
    identity_metadata("Token issuance", "critical")
    verify_login_success(identity_client)


def test_identity_known_buyer_payload_contains_email(identity_client):
    identity_metadata("Buyer identity payload")
    verify_login_success(identity_client)


def test_identity_known_buyer_payload_contains_user_id(identity_client):
    identity_metadata("Buyer id payload")
    verify_login_success(identity_client)


def test_identity_known_buyer_can_login_after_failed_attempt(identity_client):
    identity_metadata("Login recovery", "critical")
    verify_login_rejected(identity_client, "buyer@example.com", "wrong-password")
    verify_login_success(identity_client)


def test_identity_known_buyer_can_login_twice(identity_client):
    identity_metadata("Repeated login")
    verify_login_success(identity_client)
    verify_login_success(identity_client)


def test_identity_known_buyer_login_is_not_blocked_by_unknown_user(identity_client):
    identity_metadata("Unknown user isolation")
    verify_login_rejected(identity_client, "guest@example.com", "correct-password")
    verify_login_success(identity_client)


def test_identity_known_buyer_login_is_not_blocked_by_blank_email(identity_client):
    identity_metadata("Blank email recovery")
    verify_login_rejected(identity_client, "", "correct-password")
    verify_login_success(identity_client)


def test_identity_known_buyer_login_is_not_blocked_by_blank_password(identity_client):
    identity_metadata("Blank password recovery")
    verify_login_rejected(identity_client, "buyer@example.com", "")
    verify_login_success(identity_client)


def test_identity_unknown_buyer_is_rejected(identity_client):
    identity_metadata("Unknown buyer rejection")
    verify_login_rejected(identity_client, "unknown@example.com", "correct-password")


def test_identity_guest_email_is_rejected(identity_client):
    identity_metadata("Guest email rejection")
    verify_login_rejected(identity_client, "guest@example.com", "correct-password")


def test_identity_admin_email_is_rejected(identity_client):
    identity_metadata("Admin email rejection")
    verify_login_rejected(identity_client, "admin@example.com", "correct-password")


def test_identity_support_email_is_rejected(identity_client):
    identity_metadata("Support email rejection")
    verify_login_rejected(identity_client, "support@example.com", "correct-password")


def test_identity_uppercase_buyer_email_is_rejected(identity_client):
    identity_metadata("Case-sensitive email rejection")
    verify_login_rejected(identity_client, "BUYER@example.com", "correct-password")


def test_identity_buyer_email_with_alias_is_rejected(identity_client):
    identity_metadata("Alias email rejection")
    verify_login_rejected(identity_client, "buyer+demo@example.com", "correct-password")


def test_identity_buyer_email_with_leading_space_is_rejected(identity_client):
    identity_metadata("Leading whitespace rejection")
    verify_login_rejected(identity_client, " buyer@example.com", "correct-password")


def test_identity_buyer_email_with_trailing_space_is_rejected(identity_client):
    identity_metadata("Trailing whitespace rejection")
    verify_login_rejected(identity_client, "buyer@example.com ", "correct-password")


def test_identity_empty_email_is_rejected(identity_client):
    identity_metadata("Empty email rejection")
    verify_login_rejected(identity_client, "", "correct-password")


def test_identity_empty_password_is_rejected(identity_client):
    identity_metadata("Empty password rejection")
    verify_login_rejected(identity_client, "buyer@example.com", "")


def test_identity_wrong_password_is_rejected(identity_client):
    identity_metadata("Wrong password rejection", "critical")
    verify_login_rejected(identity_client, "buyer@example.com", "wrong-password")


def test_identity_old_password_is_rejected(identity_client):
    identity_metadata("Old password rejection")
    verify_login_rejected(identity_client, "buyer@example.com", "old-password")


def test_identity_short_password_is_rejected(identity_client):
    identity_metadata("Short password rejection")
    verify_login_rejected(identity_client, "buyer@example.com", "x")


def test_identity_password_with_case_change_is_rejected(identity_client):
    identity_metadata("Case-sensitive password rejection")
    verify_login_rejected(identity_client, "buyer@example.com", "Correct-Password")


def test_identity_password_with_suffix_is_rejected(identity_client):
    identity_metadata("Password suffix rejection")
    verify_login_rejected(identity_client, "buyer@example.com", "correct-password-1")


def test_identity_password_with_prefix_is_rejected(identity_client):
    identity_metadata("Password prefix rejection")
    verify_login_rejected(identity_client, "buyer@example.com", "demo-correct-password")


def test_identity_password_with_whitespace_is_rejected(identity_client):
    identity_metadata("Password whitespace rejection")
    verify_login_rejected(identity_client, "buyer@example.com", " correct-password ")


def test_identity_random_password_is_rejected(identity_client):
    identity_metadata("Random password rejection")
    verify_login_rejected(identity_client, "buyer@example.com", "a73d0d5c")


def test_identity_numeric_password_is_rejected(identity_client):
    identity_metadata("Numeric password rejection")
    verify_login_rejected(identity_client, "buyer@example.com", "123456")


def test_identity_sql_like_email_is_rejected(identity_client):
    identity_metadata("SQL-like email rejection", "critical")
    verify_login_rejected(identity_client, "' OR '1'='1", "correct-password")


def test_identity_script_like_email_is_rejected(identity_client):
    identity_metadata("Script-like email rejection", "critical")
    verify_login_rejected(identity_client, "<script@example.com", "correct-password")


def test_identity_unicode_email_is_rejected(identity_client):
    identity_metadata("Unicode email rejection")
    verify_login_rejected(identity_client, "покупатель@example.com", "correct-password")


def test_identity_locked_account_email_is_rejected(identity_client):
    identity_metadata("Locked account rejection")
    verify_login_rejected(identity_client, "locked@example.com", "correct-password")


def test_identity_deleted_account_email_is_rejected(identity_client):
    identity_metadata("Deleted account rejection")
    verify_login_rejected(identity_client, "deleted@example.com", "correct-password")


def test_identity_service_account_email_is_rejected(identity_client):
    identity_metadata("Service account rejection")
    verify_login_rejected(identity_client, "service-account@example.com", "correct-password")


def test_identity_inactive_account_email_is_rejected(identity_client):
    identity_metadata("Inactive account rejection")
    verify_login_rejected(identity_client, "inactive@example.com", "correct-password")


def test_identity_malformed_email_is_rejected(identity_client):
    identity_metadata("Malformed email rejection")
    verify_login_rejected(identity_client, "buyer.example.com", "correct-password")


def test_identity_email_without_domain_is_rejected(identity_client):
    identity_metadata("Email without domain rejection")
    verify_login_rejected(identity_client, "buyer", "correct-password")


def test_identity_success_payload_does_not_expose_password(identity_client):
    identity_metadata("Password secrecy", "critical")
    with allure.step("Login as known buyer"):
        response = identity_client.login("buyer@example.com", "correct-password")
    with allure.step("Verify password is not returned"):
        assert "password" not in response["json"]
        assert "password" not in response["json"]["user"]


def test_identity_failed_payload_does_not_expose_token(identity_client):
    identity_metadata("Rejected token secrecy", "critical")
    with allure.step("Submit rejected login"):
        response = identity_client.login("buyer@example.com", "wrong-password")
    with allure.step("Verify failed response has no token"):
        assert "token" not in response["json"]


def test_identity_session_cache_failure_demo(identity_client):
    identity_metadata("Session cache drift", "critical")
    verify_login_success(identity_client)
    pytest.fail("Demo stable failure: session cache returned an outdated account flag.")


def test_identity_audit_sink_broken_demo(identity_client):
    identity_metadata("Audit sink availability", "normal")
    verify_login_rejected(identity_client, "unknown@example.com", "correct-password")
    raise RuntimeError("Demo broken test: identity audit sink was unavailable.")
