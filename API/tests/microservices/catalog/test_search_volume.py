import allure
import pytest

from flaky import maybe_fail


LOW_SPILLOVER_FLAKY_PROBABILITY = 0.03

SEARCH_CASES = [
    *[(f"backpack-query-{index}", "backpack") for index in range(13)],
    *[(f"bottle-query-{index}", "bottle") for index in range(7)],
    *[(f"empty-query-{index}", "") for index in range(5)],
    *[(f"unknown-query-{index}", "unknown") for index in range(9)],
    ("seasonal-query-1", "summer"),
    ("seasonal-query-2", "travel"),
    ("typo-query", "bakcpack"),
]
SEARCH_CASES = [
    (case_id, query, 1 if query == "backpack" else 0)
    for case_id, query in SEARCH_CASES
]


@allure.epic("Demo Shop API")
@allure.feature("Catalog Service")
@allure.story("Product search volume")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("layer", "api")
@allure.label("component", "catalog-service")
@pytest.mark.parametrize(("case_id", "query", "expected_count"), SEARCH_CASES)
def test_catalog_search_volume(catalog_client, case_id, query, expected_count):
    with allure.step("Simulate search index stability"):
        maybe_fail(
            LOW_SPILLOVER_FLAKY_PROBABILITY,
            "neighboring catalog search index refresh delay",
        )

    with allure.step(f"Search catalog for '{query}' ({case_id})"):
        response = catalog_client.search(query)

    with allure.step("Verify search response status and result count"):
        assert response["status_code"] == 200
        assert len(response["json"]["items"]) == expected_count
