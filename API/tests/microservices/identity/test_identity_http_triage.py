from http_demo import expect_status, metadata
from triage_contracts import refresh_session


def test_web_refresh_on_expiry(http_api):
    refresh_session(http_api, 'web', 'expiry', 'profile')


def test_mobile_refresh_on_resume(http_api):
    refresh_session(http_api, 'mobile', 'resume', 'profile')


def test_app_refresh_before_checkout(http_api):
    refresh_session(http_api, 'app', 'checkout', 'orders')


def test_business_refresh_for_bulk_order(http_api):
    refresh_session(http_api, 'business', 'bulk-order', 'orders')


def test_web_refresh_after_profile_edit(http_api):
    refresh_session(http_api, 'web', 'profile-edit', 'profile')


def test_mobile_refresh_for_tracking(http_api):
    refresh_session(http_api, 'mobile', 'tracking', 'orders:read')


def test_app_refresh_for_loyalty(http_api):
    refresh_session(http_api, 'app', 'loyalty', 'rewards')


def test_web_refresh_after_key_rotation(http_api):
    refresh_session(http_api, 'web', 'key-rotation', 'profile')


def test_mobile_refresh_after_network_reconnect(http_api):
    refresh_session(http_api, 'mobile', 'reconnect', 'profile')


def test_business_refresh_for_refund(http_api):
    refresh_session(http_api, 'business', 'refund', 'orders:write')


def test_profile_has_stable_buyer_id(http_api):
    metadata('Identity', 'Profile permissions', 'identity-service')
    response = http_api.request('GET', '/identity/profile')
    expect_status(response, 200)
    assert response['json']['id'] == 'user-1'


def test_profile_has_no_admin_role(http_api):
    metadata('Identity', 'Profile permissions', 'identity-service')
    response = http_api.request('GET', '/identity/profile')
    expect_status(response, 200)
    assert 'admin' not in response['json']['roles']


def test_profile_hides_password(http_api):
    metadata('Identity', 'Profile permissions', 'identity-service')
    response = http_api.request('GET', '/identity/profile')
    expect_status(response, 200)
    assert 'password' not in response['json']


def test_recovery_does_not_expose_token(http_api):
    metadata('Identity', 'Password recovery', 'identity-service')
    response = http_api.request('POST', '/identity/password-reset', {'email': 'buyer@example.com'})
    expect_status(response, 202)
    assert 'token' not in response['json']


def test_recovery_acceptance_is_boolean(http_api):
    metadata('Identity', 'Password recovery', 'identity-service')
    response = http_api.request('POST', '/identity/password-reset', {'email': 'buyer@example.com'})
    expect_status(response, 202)
    assert response['json']['accepted'] is True


def test_session_list_has_session_identity(http_api):
    metadata('Identity', 'Session expiry', 'identity-service')
    response = http_api.request('GET', '/identity/sessions')
    expect_status(response, 200)
    assert response['json']['sessions'][0]['id'] == 'session-1'


def test_logout_response_hides_bearer_token(http_api):
    metadata('Identity', 'Session revocation', 'identity-service')
    response = http_api.request('POST', '/identity/logout', {'token': 'demo-session-secret'})
    expect_status(response, 200)
    assert 'token' not in response['json']
