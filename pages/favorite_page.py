from selene import browser, have


class FavoritePage:
    def open_shop_page(self):
        browser.open('/shop/catalogue/3/sort/a/page/1.html')
        return self

    def find_item(self):
        browser.element('[class*="_input_vn1tc_35"]').type('Python для детей. Самоучитель по программированию').press_enter()
        return self

    def open_page_item(self):
        browser.element('[class*="container"] [class="item__title"]').click()
        return self

    def click_add_to_favorites(self):
        browser.element('[class*="undefined"] [class="is-heart _icon_ogzmc_34"]').click()
        return self

    def open_favorites(self):
        browser.element('[class*="tabs-button favorite"]').click()
        return self

    def clear_favorites(self):
        browser.element('[class*="undefined"] [class="is-heart _icon_ogzmc_34"]').click()
        return self


favorite_page = FavoritePage()