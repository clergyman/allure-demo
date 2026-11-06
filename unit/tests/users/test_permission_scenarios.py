from demo_shop.users.permissions import can


import allure


pytestmark = [allure.feature('Identity'), allure.label('component', 'user-permissions')]


@allure.title("'guest' can use catalog:read")
def test_guest_catalog_read_permission():
    with allure.step('Verify role permission decision'):
        assert can('guest', 'catalog:read') is True


@allure.title("'guest' cannot use cart:write")
def test_guest_cart_write_permission():
    with allure.step('Verify role permission decision'):
        assert can('guest', 'cart:write') is False


@allure.title("'guest' cannot use order:create")
def test_guest_order_create_permission():
    with allure.step('Verify role permission decision'):
        assert can('guest', 'order:create') is False


@allure.title("'guest' cannot use product:write")
def test_guest_product_write_permission():
    with allure.step('Verify role permission decision'):
        assert can('guest', 'product:write') is False


@allure.title("'guest' cannot use support:read")
def test_guest_support_read_permission():
    with allure.step('Verify role permission decision'):
        assert can('guest', 'support:read') is False


@allure.title("'guest' cannot use admin:delete")
def test_guest_admin_delete_permission():
    with allure.step('Verify role permission decision'):
        assert can('guest', 'admin:delete') is False


@allure.title("'guest' cannot use an empty permission")
def test_guest_empty_permission_permission():
    with allure.step('Verify role permission decision'):
        assert can('guest', '') is False


@allure.title("'guest' cannot use CATALOG:READ")
def test_guest_uppercase_catalog_read_permission():
    with allure.step('Verify role permission decision'):
        assert can('guest', 'CATALOG:READ') is False


@allure.title("'customer' can use catalog:read")
def test_customer_catalog_read_permission():
    with allure.step('Verify role permission decision'):
        assert can('customer', 'catalog:read') is True


@allure.title("'customer' can use cart:write")
def test_customer_cart_write_permission():
    with allure.step('Verify role permission decision'):
        assert can('customer', 'cart:write') is True


@allure.title("'customer' can use order:create")
def test_customer_order_create_permission():
    with allure.step('Verify role permission decision'):
        assert can('customer', 'order:create') is True


@allure.title("'customer' cannot use product:write")
def test_customer_product_write_permission():
    with allure.step('Verify role permission decision'):
        assert can('customer', 'product:write') is False


@allure.title("'customer' cannot use support:read")
def test_customer_support_read_permission():
    with allure.step('Verify role permission decision'):
        assert can('customer', 'support:read') is False


@allure.title("'customer' cannot use admin:delete")
def test_customer_admin_delete_permission():
    with allure.step('Verify role permission decision'):
        assert can('customer', 'admin:delete') is False


@allure.title("'customer' cannot use an empty permission")
def test_customer_empty_permission_permission():
    with allure.step('Verify role permission decision'):
        assert can('customer', '') is False


@allure.title("'customer' cannot use CATALOG:READ")
def test_customer_uppercase_catalog_read_permission():
    with allure.step('Verify role permission decision'):
        assert can('customer', 'CATALOG:READ') is False


@allure.title("'admin' can use catalog:read")
def test_admin_catalog_read_permission():
    with allure.step('Verify role permission decision'):
        assert can('admin', 'catalog:read') is True


@allure.title("'admin' can use cart:write")
def test_admin_cart_write_permission():
    with allure.step('Verify role permission decision'):
        assert can('admin', 'cart:write') is True


@allure.title("'admin' can use order:create")
def test_admin_order_create_permission():
    with allure.step('Verify role permission decision'):
        assert can('admin', 'order:create') is True


@allure.title("'admin' can use product:write")
def test_admin_product_write_permission():
    with allure.step('Verify role permission decision'):
        assert can('admin', 'product:write') is True


@allure.title("'admin' cannot use support:read")
def test_admin_support_read_permission():
    with allure.step('Verify role permission decision'):
        assert can('admin', 'support:read') is False


@allure.title("'admin' cannot use admin:delete")
def test_admin_admin_delete_permission():
    with allure.step('Verify role permission decision'):
        assert can('admin', 'admin:delete') is False


@allure.title("'admin' cannot use an empty permission")
def test_admin_empty_permission_permission():
    with allure.step('Verify role permission decision'):
        assert can('admin', '') is False


@allure.title("'admin' cannot use CATALOG:READ")
def test_admin_uppercase_catalog_read_permission():
    with allure.step('Verify role permission decision'):
        assert can('admin', 'CATALOG:READ') is False


@allure.title('Empty role cannot use catalog:read')
def test_unrecognized_role_empty_cannot_read_catalog():
    with allure.step('Verify role permission decision'):
        assert can('', 'catalog:read') is False


@allure.title("'unknown' cannot use catalog:read")
def test_unrecognized_role_unknown_cannot_read_catalog():
    with allure.step('Verify role permission decision'):
        assert can('unknown', 'catalog:read') is False


@allure.title("'Guest' cannot use catalog:read")
def test_unrecognized_role_Guest_cannot_read_catalog():
    with allure.step('Verify role permission decision'):
        assert can('Guest', 'catalog:read') is False


@allure.title("'Customer' cannot use catalog:read")
def test_unrecognized_role_Customer_cannot_read_catalog():
    with allure.step('Verify role permission decision'):
        assert can('Customer', 'catalog:read') is False


@allure.title("'Admin' cannot use catalog:read")
def test_unrecognized_role_Admin_cannot_read_catalog():
    with allure.step('Verify role permission decision'):
        assert can('Admin', 'catalog:read') is False


@allure.title("'superuser' cannot use catalog:read")
def test_unrecognized_role_superuser_cannot_read_catalog():
    with allure.step('Verify role permission decision'):
        assert can('superuser', 'catalog:read') is False


@allure.title("'anonymous' cannot use catalog:read")
def test_unrecognized_role_anonymous_cannot_read_catalog():
    with allure.step('Verify role permission decision'):
        assert can('anonymous', 'catalog:read') is False
