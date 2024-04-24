from behave import *
from pages.checkout_code import Checkoutflow


@When('I click on checkout button')
def click_checkout(context):
    # context.driver = Checkoutflow(context.page)
    Checkoutflow.checkout(context.page)


@Then('Enter your information page should be shown and information will be filled')
def fill_information(context):
    # context.page.information_detail()
    Checkoutflow.information_detail(context.page)


@step('I click on continue button on information page')
def continue_click(context):
    # context.page.information_overview()
    Checkoutflow.information_overview(context.page)


@Then('Information overview page will be shown')
def information_check(context):
    # context.page.information_verify()
    Checkoutflow.information_verify(context.page)


@When('I click on finish button on information overview page')
def finish(context):
    # context.page.finish_click()
    Checkoutflow.finish_click(context.page)


@Then('order should get placed successfully')
def order_success(context):
    # context.page.order_check()
    Checkoutflow.order_check(context.page)

