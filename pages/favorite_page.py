from selene import browser, have


class FavoritePage:
    def open_shop_page(self):
        browser.open('/')
        return self

    def find_item(self):
        browser.element('[class*="search-field-input"]').type('100031169627').press_enter()
        return self

    def open_page_item(self):
        browser.element('button.i4a').click()
        return self

    def click_add_to_favorites(self):
        browser.element('button.i4a').click()
        return self

    def open_favorites(self):
        browser.element('[href*="/my/favorites"]').click()
        return self

    def clear_favorites(self):
        browser.element('[class*="art-buttons__drop"]').click()
        return self


favorite_page = FavoritePage()