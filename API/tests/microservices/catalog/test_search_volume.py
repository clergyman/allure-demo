import allure

from flaky import maybe_fail


LOW_SPILLOVER_FLAKY_PROBABILITY = 0.03


@allure.epic("Demo Shop")
@allure.feature("Catalog")
@allure.story("Product search volume")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "catalog-service")
def test_catalog_search_returns_backpack_for_exact_product_query(catalog_client):
    with allure.step("Simulate search index stability"):
        maybe_fail(
            LOW_SPILLOVER_FLAKY_PROBABILITY,
            "neighboring catalog search index refresh delay",
        )

    with allure.step("Search catalog for backpack"):
        response = catalog_client.search("backpack")

    with allure.step("Verify exact product search returns one matching item"):
        assert response["status_code"] == 200
        assert response["json"]["items"] == [
            {"id": "product-1", "name": "Demo Backpack"}
        ]


@allure.epic("Demo Shop")
@allure.feature("Catalog")
@allure.story("Product search volume")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "catalog-service")
def test_catalog_search_returns_empty_result_for_unknown_product(catalog_client):
    with allure.step("Search catalog for an unknown product"):
        response = catalog_client.search("travel mug")

    with allure.step("Verify unknown products do not leak stale matches"):
        assert response["status_code"] == 200
        assert response["json"]["items"] == []


@allure.epic("Demo Shop")
@allure.feature("Catalog")
@allure.story("Product search volume")
@allure.severity("minor")
@allure.label("layer", "api")
@allure.label("component", "catalog-service")
def test_catalog_search_handles_blank_query_as_empty_result(catalog_client):
    with allure.step("Search catalog with a blank query"):
        response = catalog_client.search("")

    with allure.step("Verify blank search is accepted but returns no products"):
        assert response["status_code"] == 200
        assert response["json"]["items"] == []
