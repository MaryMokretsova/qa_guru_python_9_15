import allure
from pages.main_menu_page import main_menu_page
from pages.search_page import search_page


class TestSearch:

    def test_header_search_positive(self, browser_management):
        with allure.step("Open marketplace"):
            main_menu_page.open_shop_page()
        with allure.step("Input text for search"):
            search_page.header_search('Тетради')
        with allure.step("Check the result of an successful search"):
            search_page.search_result_success('Тетради')

    def test_header_search_negative(self, browser_management):
        with allure.step("Open marketplace"):
            main_menu_page.open_shop_page()
        with allure.step("Input text for search"):
            search_page.header_search('asddfgrhtjykykk')
        with allure.step("Check the result of an unsuccessful search"):
            search_page.search_result_failure('По вашему запросу ничего не найдено. Возможно, вам понравятся эти ')
