from selene.support import by
from selene.support.conditions import be
from selene import browser


def test_github(setup_browser):
    browser = setup_browser
    browser.open("https://github.com/")

    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys("Letstakeyride/test_for_qa_guru")
    browser.element(".header-search-input").submit()

    browser.element(by.link_text("Letstakeyride/test_for_qa_guru")).click()
    browser.element("#issues-tab").click()

    # browser.element(by.partial_text("#1")).should(be.visible)
