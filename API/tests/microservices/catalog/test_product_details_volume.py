import allure

from flaky import maybe_fail


@allure.epic("Demo Shop")
@allure.feature("Catalog")
@allure.story("Product detail volume")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "catalog-service")
def test_catalog_product_details_include_available_backpack_stock(catalog_client):
    with allure.step("Simulate catalog read stability"):
        maybe_fail(0, "catalog read replica lag")

    with allure.step("Request backpack details"):
        response = catalog_client.get_product("product-1")

    with allure.step("Verify product identity and inventory are returned"):
        assert response["status_code"] == 200
        assert response["json"]["name"] == "Demo Backpack"
        assert response["json"]["stock"] == 12


@allure.epic("Demo Shop")
@allure.feature("Catalog")
@allure.story("Product detail volume")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "catalog-service")
def test_catalog_product_details_show_out_of_stock_bottle(catalog_client):
    with allure.step("Request bottle details"):
        response = catalog_client.get_product("product-2")

    with allure.step("Verify out-of-stock products are still visible"):
        assert response["status_code"] == 200
        assert response["json"]["name"] == "Demo Bottle"
        assert response["json"]["stock"] == 0


@allure.epic("Demo Shop")
@allure.feature("Catalog")
@allure.story("Product detail volume")
@allure.severity("minor")
@allure.label("layer", "api")
@allure.label("component", "catalog-service")
def test_catalog_product_details_return_not_found_for_missing_product(catalog_client):
    with allure.step("Request a product id that is not in the catalog"):
        response = catalog_client.get_product("missing-product-13")

    with allure.step("Verify missing product response"):
        assert response["status_code"] == 404
        assert response["json"]["error"] == "Product not found"
