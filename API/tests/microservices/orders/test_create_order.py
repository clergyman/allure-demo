def test_create_order_returns_created_order(orders_client):
    response = orders_client.create_order(
        user_id="user-1",
        product_id="product-1",
        quantity=2,
    )

    assert response["status_code"] == 201
    assert response["json"]["status"] == "created"


def test_create_order_rejects_zero_quantity(orders_client):
    response = orders_client.create_order(
        user_id="user-1",
        product_id="product-1",
        quantity=0,
    )

    assert response["status_code"] == 400

