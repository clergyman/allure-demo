def test_get_order_returns_status(orders_client):
    response = orders_client.get_order("order-1")

    assert response["status_code"] == 200
    assert response["json"]["status"] == "created"


def test_get_order_returns_not_found_for_unknown_order(orders_client):
    response = orders_client.get_order("missing-order")

    assert response["status_code"] == 404

