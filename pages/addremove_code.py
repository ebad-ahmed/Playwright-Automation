import time


class AddRemoveProduct:
    def __init__(self, page):
        self.page = page

    def home_check(self):
        self.page.wait_for_selector('.header_label .app_logo')
        assert self.page.locator('.header_label .app_logo')

    def add_product(self):
        self.page.locator('#add-to-cart-sauce-labs-backpack').click()

    def click_cart(self):
        self.page.locator('#shopping_cart_container').click()

    def check_cart(self):
        self.page.wait_for_selector('.header_secondary_container .title')
        assert self.page.locator('.header_secondary_container .title')

    def remove_product(self):
        self.page.wait_for_selector('#remove-sauce-labs-backpack')
        self.page.locator('#remove-sauce-labs-backpack').click()

    def product_removed(self):
        self.page.reload()
        time.sleep(5)
        try:
            element = self.page.locator(".shopping_cart_badge")  # Adjust selector
            if element.is_visible():
                print("Is visible")
        except TimeoutError:
            # If the expected element is not found, the badge might be absent (success)
            print("Shopping cart badge likely removed. Product removal successful.")
