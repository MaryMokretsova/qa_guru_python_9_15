import allure

from pages import search_page
from pages.search_page import SearchPage

from pages.favorite_page import favorite_page


search_page = SearchPage()


class TestSearch:

    def test_header_search_positive(self, browser_management):
        with allure.step("Open marketplace"):
            favorite_page.open_shop_page()
        with allure.step("Input text for search"):
            search_page.header_search('Тетради')
        with allure.step("Check the result of an successful search"):
            search_page.search_result_success('Тетради')

    def test_header_search_negative(self, browser_management):
        with allure.step("Open marketplace"):
            favorite_page.open_shop_page()
        with allure.step("Input text for search"):
            search_page.header_search('asddfgrhtjykykk')
        with allure.step("Check the result of an unsuccessful search"):
            search_page.search_result_failure('По вашему запросу ничего не найдено. Возможно, вам понравятся эти ')
