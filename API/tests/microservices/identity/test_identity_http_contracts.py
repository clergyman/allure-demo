import allure

from http_demo import expect_status, metadata


def test_password_reset_is_accepted(http_api):
    metadata('Identity', 'Password recovery', 'identity-service')
    response = http_api.request('POST', '/identity/password-reset', {'email': 'buyer@example.com'})
    expect_status(response, 202)
    assert response['json']['accepted']


def test_buyer_profile_contains_role(http_api):
    metadata('Identity', 'Profile permissions', 'identity-service')
    response = http_api.request('GET', '/identity/profile')
    expect_status(response, 200)
    assert response['json']['roles'] == ['buyer']


def test_logout_revokes_session(http_api):
    metadata('Identity', 'Session revocation', 'identity-service')
    expect_status(http_api.request('GET', '/identity/profile'), 200)
    response = http_api.request('POST', '/identity/logout', {'token': 'demo-session-token'})
    expect_status(response, 200)
    assert response['json']['revoked']


def test_valid_mfa_challenge_is_verified(http_api):
    metadata('Identity', 'Multi-factor authentication', 'identity-service')
    response = http_api.request('POST', '/identity/mfa/verify', {'challenge': 'challenge-1', 'otp': '123456'})
    expect_status(response, 200)
    with allure.step('Verify valid challenge accepted'):
        assert response['json']['verified'], response['json']['reason']


def test_refresh_survives_key_rotation(http_api):
    metadata('Identity', 'Token rotation', 'identity-service')
    response = http_api.request('POST', '/identity/token/refresh', {'refresh_token': 'demo-refresh-secret'})
    expect_status(response, 200)


def test_session_expiry_contract(http_api):
    metadata('Identity', 'Session expiry', 'identity-service')
    response = http_api.request('GET', '/identity/sessions')
    expect_status(response, 200)
    with allure.step('Read session expiration field'):
        assert response['json']['sessions'][0]['expires_at'].endswith('Z')
