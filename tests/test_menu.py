import allure
from pages.main_page import main_page


class TestMenu:

    def test_main_menu(self):
        with allure.step("Open marketplace"):
            main_page.open_shop_page()
        with allure.step("Checking first level menu items"):
            main_page.assert_header_main_menu()
        with allure.step("Checking second level menu items"):
            main_page.assert_body_main_menu()
        with allure.step("Checking third level menu items"):
            main_page.assert_footer_main_menu()
