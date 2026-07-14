import allure
import pytest


@allure.epic("Demo Shop API")
@allure.feature("Catalog Service")
@allure.story("Product details")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("layer", "api")
@allure.label("component", "catalog-service")
def test_get_product_returns_product_details(catalog_client):
    with allure.step("Request an existing product by id"):
        response = catalog_client.get_product("product-1")

    with allure.step("Verify product details are returned"):
        assert response["status_code"] == 200
        assert response["json"]["name"] == "Demo Backpack"
        pytest.fail(
            "Demo stable failure: catalog inventory projection returned stale stock."
        )


@allure.epic("Demo Shop API")
@allure.feature("Catalog Service")
@allure.story("Product details")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("layer", "api")
@allure.label("component", "catalog-service")
def test_get_product_returns_not_found_for_unknown_product(catalog_client):
    with allure.step("Request a missing product by id"):
        response = catalog_client.get_product("missing-product")

    with allure.step("Verify the catalog service returns not found"):
        assert response["status_code"] == 404
