def test_get_product_returns_product_details(catalog_client):
    response = catalog_client.get_product("product-1")

    assert response["status_code"] == 200
    assert response["json"]["name"] == "Demo Backpack"
    assert response["json"]["stock"] == 12


def test_get_product_returns_not_found_for_unknown_product(catalog_client):
    response = catalog_client.get_product("missing-product")

    assert response["status_code"] == 404

