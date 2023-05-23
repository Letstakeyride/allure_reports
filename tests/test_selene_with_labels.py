import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene import browser


@allure.tag("web")
@allure.label("owner", "agargalyk")
@allure.feature("Поиск в git")
@allure.story("Ищем issue в репозитории git")
@allure.link("https://github.com", name="Testing")
def test_github(setup_browser):
    with allure.step('Открываем гит'):
        browser.open("https://github.com/")
    with allure.step('Ищем репозиторий'):
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").send_keys("Letstakeyride/test_for_qa_guru")
        browser.element(".header-search-input").submit()
    with allure.step('Открываем issue'):
        browser.element(by.link_text("Letstakeyride/test_for_qa_guru")).click()
        browser.element("#issues-tab").click()
    with allure.step('Проверяем наличие issue'):
        browser.element(by.partial_text("#1")).should(be.visible)
