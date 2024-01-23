import allure
from selene import browser, have
import time


class SearchPage:

    @allure.step('Ввести в поле поиска {text}')
    def header_search(self, text):
        browser.element('[class*="_input_vn1tc_35"]').type(text).press_enter()
        time.sleep(5)

    @allure.step('Проверить результат успешного поиска')
    def search_result_success(self, text):
        browser.element('[class*="h1"] [class="title"]').should(have.text(text))

    @allure.step('Проверить результат неуспешного поиска')
    def search_result_failure(self, text):
        browser.element('[class*="search-type"] [class="search-type__text"]').should(have.text(text))


search_page = SearchPage()