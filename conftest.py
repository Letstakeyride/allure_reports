from selene import browser
import pytest


@pytest.fixture(scope="function", autouse=True)
def init_browser():
    browser.driver().set_window_size(1920, 1080)
    yield
    browser.quit()
