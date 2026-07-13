def test_search_finds_matching_product(catalog_client):
    response = catalog_client.search("backpack")

    assert response["status_code"] == 200
    assert response["json"]["items"][0]["name"] == "Demo Backpack"


def test_search_returns_empty_list_when_nothing_matches(catalog_client):
    response = catalog_client.search("spaceship")

    assert response["status_code"] == 200
    assert response["json"]["items"] == []

