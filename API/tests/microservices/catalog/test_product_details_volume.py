import allure
import pytest

from flaky import maybe_fail


PRODUCT_CASES = [
    *[
        (f"backpack-detail-{index}", "product-1", 200)
        for index in range(19)
    ],
    *[
        (f"bottle-detail-{index}", "product-2", 200)
        for index in range(11)
    ],
    *[
        (f"missing-detail-{index}", f"missing-product-{index}", 404)
        for index in (2, 3, 5, 8, 13)
    ],
]


@allure.epic("Demo Shop")
@allure.feature("Catalog")
@allure.story("Product detail volume")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "catalog-service")
@pytest.mark.parametrize(("case_id", "product_id", "expected_status"), PRODUCT_CASES)
def test_catalog_product_details_volume(
    catalog_client, case_id, product_id, expected_status
):
    with allure.step("Simulate catalog read stability"):
        maybe_fail(0, "catalog read replica lag")

    with allure.step(f"Request product {product_id} ({case_id})"):
        response = catalog_client.get_product(product_id)

    with allure.step("Verify product response status"):
        assert response["status_code"] == expected_status
