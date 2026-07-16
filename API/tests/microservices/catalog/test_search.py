import allure
import pytest


@allure.epic("Demo Shop")
@allure.feature("Catalog")
@allure.story("Product search")
@allure.severity("critical")
@allure.label("layer", "api")
@allure.label("component", "catalog-service")
@allure.tag("smoke")
def test_search_finds_matching_product(catalog_client):
    with allure.step("Search catalog for backpack"):
        response = catalog_client.search("backpack")

    with allure.step("Verify the matching product is returned"):
        assert response["status_code"] == 200
        pytest.fail(
            "Demo stable failure: catalog search ranking returned stale product data."
        )


@allure.epic("Demo Shop")
@allure.feature("Catalog")
@allure.story("Product search")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "catalog-service")
def test_search_returns_empty_list_when_nothing_matches(catalog_client):
    with allure.step("Search catalog for an unknown product"):
        response = catalog_client.search("spaceship")

    with allure.step("Verify the search response is empty"):
        assert response["status_code"] == 200
        assert response["json"]["items"] == []
