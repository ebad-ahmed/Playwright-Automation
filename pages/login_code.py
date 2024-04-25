from pages.BasePage import BasePage


class LoginCode(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def goto_page(self):
        self.open_url('https://www.saucedemo.com/')

    def add_credentials(self):
        # self.page.fill('#user-name', 'standard_user')
        # self.page.fill('#password', 'secret_sauce')
        self.type_into_element('id', 'user-name', 'standard_user')
        self.type_into_element('id', 'password', 'secret_sauce')

    def submit_the_form(self):
        # self.page.press('#login-button', 'Enter')
        self.click_on_element('id', 'login-button')

    def check_data(self):
        # self.page.wait_for_selector(".header_secondary_container .title")
        # assert self.page.locator(".header_secondary_container .title")
        self.retrieved_element_text_contains('css', '.title', 'Products')
