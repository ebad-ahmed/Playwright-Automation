import time
from pages.BasePage import BasePage


class AddRemoveProduct(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def home_check(self):
        # self.page.wait_for_selector('.header_label .app_logo')
        # assert self.page.locator('.header_label .app_logo')
        self.retrieved_element_text_contains('css', '.header_label .app_logo', 'Swag Labs')

    def add_product(self):
        # self.page.locator('#add-to-cart-sauce-labs-backpack').click()
        self.click_on_element('id', 'add-to-cart-sauce-labs-backpack')

    def click_cart(self):
        # self.page.locator('#shopping_cart_container').click()
        self.click_on_element('id', 'shopping_cart_container')

    def check_cart(self):
        # self.page.wait_for_selector('.header_secondary_container .title')
        # assert self.page.locator('.header_secondary_container .title')
        self.retrieved_element_text_contains('css', '.header_secondary_container .title', 'Your Cart')

    def remove_product(self):
        # self.page.wait_for_selector('#remove-sauce-labs-backpack')
        # self.page.locator('#remove-sauce-labs-backpack').click()
        self.click_on_element('id', 'remove-sauce-labs-backpack')

    def product_removed(self):
        self.page.reload()
        time.sleep(5)
        try:
            # element = self.page.locator(".shopping_cart_badge")  # Adjust selector
            check = self.page.locator('.shopping_cart_badge')
            # check = self.get_element('css', '.shopping_cart_badge')
            if check.is_visible():
                print("Is visible")
        except TimeoutError:
            # If the expected element is not found, the badge might be absent (success)
            print("Shopping cart badge likely removed. Product removal successful.")
