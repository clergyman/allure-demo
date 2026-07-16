import allure
import pytest

from demo_shop.users.permissions import ROLE_PERMISSIONS, can

pytestmark = [
    allure.label("component", "user-permissions"),
]

PERMISSION_CASES = [
    (role, permission, permission in ROLE_PERMISSIONS[role])
    for role in ROLE_PERMISSIONS
    for permission in [
        "catalog:read",
        "cart:write",
        "order:create",
        "product:write",
        "support:read",
        "admin:delete",
    ]
]

UNKNOWN_ROLE_CASES = [
    (f"unknown-role-{index}", "catalog:read") for index in range(20)
]


@pytest.mark.parametrize(("role", "permission", "expected"), PERMISSION_CASES)
def test_role_permission_matrix(role, permission, expected):
    with allure.step("Verify role permission lookup"):
        assert can(role, permission) is expected


@pytest.mark.parametrize(("role", "permission"), UNKNOWN_ROLE_CASES)
def test_unknown_roles_have_no_permissions(role, permission):
    with allure.step("Verify unknown role has no permissions"):
        assert can(role, permission) is False
