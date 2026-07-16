import allure
import pytest


@pytest.fixture(autouse=True)
def unit_layer_label():
    allure.dynamic.label("layer", "unit")
