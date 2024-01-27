import allure
from pages.main_menu_page import main_menu_page


class TestMainMenu:

    def test_main_menu(self, browser_management):
        with allure.step("Open marketplace"):
            main_menu_page.open_shop_page()
        with allure.step("Checking first level menu items"):
            main_menu_page.assert_header_main_menu()
        with allure.step("Checking second level menu items"):
            main_menu_page.assert_body_main_menu()
        with allure.step("Checking third level menu items"):
            main_menu_page.assert_footer_main_menu()
