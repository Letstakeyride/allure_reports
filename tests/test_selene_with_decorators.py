import allure
from selene.support import by
from selene.support.conditions import be
from selene import browser


def test_decorator_steps():
    open_main_page()
    search_for_repository("Letstakeyride/test_for_qa_guru")
    open_issue_tab()
    should_see_issue_with_number("#1")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys("Letstakeyride/test_for_qa_guru")
    browser.element(".header-search-input").submit()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element(by.link_text("Letstakeyride/test_for_qa_guru")).click()
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)
