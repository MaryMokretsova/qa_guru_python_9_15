import allure
from pages.cart_page import cart_page
from pages.main_menu_page import main_menu_page


class TestCart:

    @allure.title("Adding and removing a book to cart")
    def test_item_add_and_delete_cart(self, browser_management):
        with allure.step("Open marketplace"):
            main_menu_page.open_shop_page()
        with allure.step("Book search"):
            cart_page.find_item()
        with allure.step("Open product page"):
            cart_page.open_page_item()
        with allure.step("Click add to cart"):
            cart_page.click_add_to_cart()
        with allure.step("Open cart"):
            cart_page.open_cart()
        with allure.step("Clear cart"):
            cart_page.clear_cart()
        with allure.step("Confirm clear cart"):
            cart_page.confirm_clear_cart()
        with allure.step("Assert text cart"):
            cart_page.assert_page_cart()
