import allure
from selene.support import by
from selene.support.conditions import be
from selene import browser


def test_github():
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
