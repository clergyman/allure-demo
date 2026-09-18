import allure
import pytest
import traceback

from clients.catalog_client import CatalogClient
from clients.identity_client import IdentityClient
from clients.orders_client import OrdersClient
from http_demo import HttpDemoClient, start_server
from triage_contracts import TriageDefect


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_makereport(item, call):
    report = (yield).get_result()
    if call.when != 'call' or not call.excinfo or not isinstance(call.excinfo.value, TriageDefect):
        return
    allure.attach(report.longreprtext, name='Full pytest traceback',
                  attachment_type=allure.attachment_type.TEXT)
    # Drop scenario caller frames for exact root-cause grouping, keeping the
    # actual shared validator traceback and the full original trace attached.
    tb = call.excinfo.value.__traceback__
    while tb and not tb.tb_frame.f_code.co_name.startswith('verify_'):
        tb = tb.tb_next
    if tb:
        report.longrepr = ''.join(traceback.format_exception(type(call.excinfo.value), call.excinfo.value, tb))


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
