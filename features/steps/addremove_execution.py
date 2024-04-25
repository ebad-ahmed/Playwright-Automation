from behave import *
from pages.addremove_code import AddRemoveProduct



@Given('I am on the home page')
def on_home(context):
    context.page = AddRemoveProduct(context.page)
    context.page.home_check()


@When('I add a product to cart')
def add_product(context):
    context.page.add_product()


@step('I click cart icon to go on cart page')
def goto_cart(context):
    context.page.click_cart()


@Then('I should be redirected to the cart page')
def verify_cart(context):
    context.page.check_cart()


@When('I click on remove button on cart page')
def click_remove(context):
    context.page.remove_product()


@Then('product should be removed')
def product_remove(context):
    context.page.product_removed()
