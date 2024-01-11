import pytest
from selene import browser

@pytest.fixture(scope="function", autouse=True)
def set_driver():
    browser.config.window_width = 1920
    browser.config.window_height = 720
    yield browser
    browser.quit()