

class LoginCode:

    def __init__(self, page):
        self.page = page

    def goto_page(self):
        self.page.goto('https://www.saucedemo.com/')

    def add_credentials(self):
        self.page.fill('#user-name', 'standard_user')
        self.page.fill('#password', 'secret_sauce')

    def submit_the_form(self):
        self.page.press('#login-button', 'Enter')
    #

    def check_data(self):
        self.page.wait_for_selector(".header_secondary_container .title")
        assert self.page.locator(".header_secondary_container .title")
