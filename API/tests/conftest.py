import allure
import pytest

from clients.catalog_client import CatalogClient
from clients.identity_client import IdentityClient
from clients.orders_client import OrdersClient


@pytest.fixture(autouse=True)
def api_layer_label():
    allure.dynamic.label("layer", "api")


@pytest.fixture
def identity_client():
    return IdentityClient()


@pytest.fixture
def catalog_client():
    return CatalogClient()


@pytest.fixture
def orders_client():
    return OrdersClient()
