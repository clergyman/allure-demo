import allure
import pytest


def catalog_metadata(story: str, severity: str = "normal"):
    allure.dynamic.epic("Demo Shop")
    allure.dynamic.feature("Catalog")
    allure.dynamic.story(story)
    allure.dynamic.severity(severity)
    allure.dynamic.label("component", "catalog-service")


def verify_product(catalog_client, product_id: str, expected_name: str, expected_stock: int):
    with allure.step(f"Request product details for {product_id}"):
        response = catalog_client.get_product(product_id)

    with allure.step("Verify catalog product payload"):
        assert response["status_code"] == 200
        assert response["json"]["id"] == product_id
        assert response["json"]["name"] == expected_name
        assert response["json"]["stock"] == expected_stock


def verify_missing_product(catalog_client, product_id: str):
    with allure.step(f"Request missing product {product_id}"):
        response = catalog_client.get_product(product_id)

    with allure.step("Verify missing product contract"):
        assert response["status_code"] == 404
        assert response["json"]["error"] == "Product not found"


def verify_search_count(catalog_client, query: str, expected_count: int):
    with allure.step(f"Search catalog for {query!r}"):
        response = catalog_client.search(query)

    with allure.step("Verify search result count"):
        assert response["status_code"] == 200
        assert len(response["json"]["items"]) == expected_count


def test_catalog_backpack_product_has_expected_identity(catalog_client):
    catalog_metadata("Backpack product card", "critical")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)


def test_catalog_backpack_product_exposes_positive_stock(catalog_client):
    catalog_metadata("Backpack stock visibility")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)


def test_catalog_backpack_product_keeps_stable_product_id(catalog_client):
    catalog_metadata("Backpack product identity")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)


def test_catalog_backpack_product_name_is_customer_facing(catalog_client):
    catalog_metadata("Backpack merchandising")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)


def test_catalog_backpack_product_can_be_requested_after_cache_warmup(catalog_client):
    catalog_metadata("Backpack cache warmup")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)


def test_catalog_backpack_product_can_be_requested_from_listing_context(catalog_client):
    catalog_metadata("Backpack listing handoff")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)


def test_catalog_backpack_product_supports_checkout_handoff(catalog_client):
    catalog_metadata("Backpack checkout handoff", "critical")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)


def test_catalog_backpack_product_supports_search_handoff(catalog_client):
    catalog_metadata("Backpack search handoff")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)


def test_catalog_backpack_product_stock_is_not_negative(catalog_client):
    catalog_metadata("Backpack inventory guard")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)


def test_catalog_backpack_product_contract_survives_second_read(catalog_client):
    catalog_metadata("Backpack repeated read")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)


def test_catalog_bottle_product_has_expected_identity(catalog_client):
    catalog_metadata("Bottle product card")
    verify_product(catalog_client, "product-2", "Demo Bottle", 0)


def test_catalog_bottle_product_exposes_zero_stock(catalog_client):
    catalog_metadata("Bottle stock visibility")
    verify_product(catalog_client, "product-2", "Demo Bottle", 0)


def test_catalog_bottle_product_remains_visible_when_unavailable(catalog_client):
    catalog_metadata("Out of stock visibility")
    verify_product(catalog_client, "product-2", "Demo Bottle", 0)


def test_catalog_bottle_product_keeps_stable_product_id(catalog_client):
    catalog_metadata("Bottle product identity")
    verify_product(catalog_client, "product-2", "Demo Bottle", 0)


def test_catalog_bottle_product_does_not_report_backpack_stock(catalog_client):
    catalog_metadata("Bottle inventory isolation")
    verify_product(catalog_client, "product-2", "Demo Bottle", 0)


def test_catalog_bottle_product_can_be_requested_after_backpack(catalog_client):
    catalog_metadata("Mixed product read")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)
    verify_product(catalog_client, "product-2", "Demo Bottle", 0)


def test_catalog_missing_product_returns_not_found_for_retired_sku(catalog_client):
    catalog_metadata("Missing retired SKU")
    verify_missing_product(catalog_client, "retired-product-1")


def test_catalog_missing_product_returns_not_found_for_supplier_sku(catalog_client):
    catalog_metadata("Missing supplier SKU")
    verify_missing_product(catalog_client, "supplier-product-9")


def test_catalog_missing_product_returns_not_found_for_empty_slot(catalog_client):
    catalog_metadata("Missing empty slot")
    verify_missing_product(catalog_client, "empty-slot-4")


def test_catalog_missing_product_returns_not_found_for_deleted_sku(catalog_client):
    catalog_metadata("Missing deleted SKU")
    verify_missing_product(catalog_client, "deleted-product-12")


def test_catalog_missing_product_returns_not_found_for_future_sku(catalog_client):
    catalog_metadata("Missing future SKU")
    verify_missing_product(catalog_client, "future-product-2027")


def test_catalog_missing_product_returns_not_found_for_external_sku(catalog_client):
    catalog_metadata("Missing external SKU")
    verify_missing_product(catalog_client, "external-marketplace-2")


def test_catalog_search_backpack_exact_match_returns_one_item(catalog_client):
    catalog_metadata("Backpack search relevance", "critical")
    verify_search_count(catalog_client, "backpack", 1)


def test_catalog_search_backpack_repeat_returns_one_item(catalog_client):
    catalog_metadata("Backpack repeated search")
    verify_search_count(catalog_client, "backpack", 1)


def test_catalog_search_backpack_after_blank_query_returns_one_item(catalog_client):
    catalog_metadata("Backpack search recovery")
    verify_search_count(catalog_client, "", 0)
    verify_search_count(catalog_client, "backpack", 1)


def test_catalog_search_unknown_product_returns_empty_list(catalog_client):
    catalog_metadata("Unknown product search")
    verify_search_count(catalog_client, "charger", 0)


def test_catalog_search_typo_returns_empty_list(catalog_client):
    catalog_metadata("Typo product search")
    verify_search_count(catalog_client, "bakcpack", 0)


def test_catalog_search_seasonal_term_returns_empty_list(catalog_client):
    catalog_metadata("Seasonal search")
    verify_search_count(catalog_client, "summer", 0)


def test_catalog_search_blank_query_returns_empty_list(catalog_client):
    catalog_metadata("Blank search")
    verify_search_count(catalog_client, "", 0)


def test_catalog_search_spaces_query_returns_empty_list(catalog_client):
    catalog_metadata("Whitespace search")
    verify_search_count(catalog_client, "   ", 0)


def test_catalog_search_uppercase_backpack_is_currently_case_sensitive(catalog_client):
    catalog_metadata("Case-sensitive search")
    verify_search_count(catalog_client, "BACKPACK", 1)


def test_catalog_search_bottle_does_not_return_unavailable_product(catalog_client):
    catalog_metadata("Unavailable product search")
    verify_search_count(catalog_client, "bottle", 0)


def test_catalog_search_travel_term_returns_empty_list(catalog_client):
    catalog_metadata("Travel search")
    verify_search_count(catalog_client, "travel", 0)


def test_catalog_search_accessory_term_returns_empty_list(catalog_client):
    catalog_metadata("Accessory search")
    verify_search_count(catalog_client, "strap", 0)


def test_catalog_search_long_tail_term_returns_empty_list(catalog_client):
    catalog_metadata("Long-tail search")
    verify_search_count(catalog_client, "waterproof day pack", 0)


def test_catalog_search_numeric_term_returns_empty_list(catalog_client):
    catalog_metadata("Numeric search")
    verify_search_count(catalog_client, "12345", 0)


def test_catalog_search_symbol_term_returns_empty_list(catalog_client):
    catalog_metadata("Symbol search")
    verify_search_count(catalog_client, "#sale", 0)


def test_catalog_search_backpack_payload_contains_product_name(catalog_client):
    catalog_metadata("Backpack search payload")
    with allure.step("Search catalog for backpack"):
        response = catalog_client.search("backpack")
    with allure.step("Verify returned product name"):
        assert response["json"]["items"][0]["name"] == "Demo Backpack"


def test_catalog_search_backpack_payload_contains_product_id(catalog_client):
    catalog_metadata("Backpack search product id")
    with allure.step("Search catalog for backpack"):
        response = catalog_client.search("backpack")
    with allure.step("Verify returned product id"):
        assert response["json"]["items"][0]["id"] == "product-1"


def test_catalog_search_result_does_not_include_out_of_stock_bottle(catalog_client):
    catalog_metadata("Search stock filter")
    with allure.step("Search catalog for backpack"):
        response = catalog_client.search("backpack")
    with allure.step("Verify out-of-stock bottle is not included"):
        assert all(item["name"] != "Demo Bottle" for item in response["json"]["items"])


def test_catalog_search_empty_result_has_items_collection(catalog_client):
    catalog_metadata("Empty search shape")
    with allure.step("Search catalog for unknown product"):
        response = catalog_client.search("unknown")
    with allure.step("Verify empty result shape"):
        assert response["json"]["items"] == []


def test_catalog_backpack_inventory_projection_failure_demo(catalog_client):
    catalog_metadata("Inventory projection drift", "critical")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)
    pytest.fail("Demo stable failure: inventory projection still shows yesterday's stock.")


def test_catalog_search_ranking_failure_demo(catalog_client):
    catalog_metadata("Search ranking drift", "critical")
    verify_search_count(catalog_client, "backpack", 1)
    pytest.fail("Demo stable failure: search ranking promoted a stale catalog document.")


def test_catalog_price_index_broken_demo(catalog_client):
    catalog_metadata("Price index availability", "normal")
    verify_product(catalog_client, "product-1", "Demo Backpack", 12)
    raise RuntimeError("Demo broken test: price index response was missing from fixture.")
