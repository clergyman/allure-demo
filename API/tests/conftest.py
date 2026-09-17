import allure
import pytest

from clients.catalog_client import CatalogClient
from clients.identity_client import IdentityClient
from clients.orders_client import OrdersClient
from http_demo import HttpDemoClient, start_server


@pytest.fixture(scope='session')
def http_api():
    server, thread = start_server()
    try:
        yield HttpDemoClient(f'http://127.0.0.1:{server.server_port}')
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


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
