import time
from playwright.sync_api import expect
class Checkoutflow:
    def __init__(self, page):
        self.page = page

    def checkout(self):
        self.page.wait_for_selector('#checkout')
        self.page.locator('#checkout').click()

    def information_detail(self):
        self.page.reload()
        time.sleep(2)
        page_title = self.page.locator("#header_container > div.header_secondary_container > span")
        expect(page_title).to_have_text("Checkout: Your Information")
        self.page.fill('#first-name', 'testing')
        self.page.fill('#last-name', 'testing')
        self.page.fill('#postal-code', '75300')

    def information_overview(self):
        self.page.locator('#continue').click()

    def information_verify(self):
        self.page.locator('.summary_total_label')
        assert self.page.locator('.summary_total_label')
        text_verify = self.page.locator("#header_container > div.header_secondary_container > span")
        expect(text_verify).to_have_text("Checkout: Overview")

    def finish_click(self):
        self.page.wait_for_selector('#finish')
        self.page.locator('#finish').click()

    def order_check(self):
        self.page.reload()
        title_locator = self.page.locator("#checkout_complete_container > h2")
        expect(title_locator).to_have_text("Thank you for your order!")
