import pytest

from flaky import maybe_fail


LOGIN_CASES = [
    (f"buyer-{index}@example.com", "correct-password", 401)
    for index in range(30)
] + [("buyer@example.com", "correct-password", 200) for _ in range(10)]

PRODUCT_CASES = [
    ("product-1", 200),
    ("product-2", 200),
] * 20

SEARCH_CASES = [
    (["backpack", "bottle", "unknown", ""])[index % 4]
    for index in range(40)
]
SEARCH_CASES = [
    (query, 1 if query == "backpack" else 0)
    for query in SEARCH_CASES
]

ORDER_CASES = [
    ("user-1", "product-1", quantity, 201 if quantity > 0 else 400)
    for quantity in range(-10, 40)
] * 1

ORDER_STATUS_CASES = [
    ("order-1", 200),
    *[(f"missing-order-{index}", 404) for index in range(19)],
]

RARE_FLAKY_PROBABILITY = 0.001


@pytest.mark.parametrize(("email", "password", "expected_status"), LOGIN_CASES)
def test_volume_identity_login(identity_client, email, password, expected_status):
    maybe_fail(RARE_FLAKY_PROBABILITY, "identity session cache timed out")

    response = identity_client.login(email, password)

    assert response["status_code"] == expected_status


@pytest.mark.parametrize(("product_id", "expected_status"), PRODUCT_CASES)
def test_volume_catalog_products(catalog_client, product_id, expected_status):
    maybe_fail(RARE_FLAKY_PROBABILITY, "catalog read replica lag")

    response = catalog_client.get_product(product_id)

    assert response["status_code"] == expected_status


@pytest.mark.parametrize(("query", "expected_count"), SEARCH_CASES)
def test_volume_catalog_search(catalog_client, query, expected_count):
    maybe_fail(RARE_FLAKY_PROBABILITY, "search index refresh delay")

    response = catalog_client.search(query)

    assert response["status_code"] == 200
    assert len(response["json"]["items"]) == expected_count


@pytest.mark.parametrize(
    ("user_id", "product_id", "quantity", "expected_status"), ORDER_CASES
)
def test_volume_order_creation(
    orders_client, user_id, product_id, quantity, expected_status
):
    maybe_fail(RARE_FLAKY_PROBABILITY, "order queue accepted late")

    response = orders_client.create_order(user_id, product_id, quantity)

    assert response["status_code"] == expected_status


@pytest.mark.parametrize(("order_id", "expected_status"), ORDER_STATUS_CASES)
def test_volume_order_status(orders_client, order_id, expected_status):
    maybe_fail(RARE_FLAKY_PROBABILITY, "order projection not ready")

    response = orders_client.get_order(order_id)

    assert response["status_code"] == expected_status
