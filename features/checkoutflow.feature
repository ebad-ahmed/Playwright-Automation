Feature: To verify that product checkout flow is working
  As a standard user
  I want to add product to cart the and then complete the checkout process

  Background:
    Given I am on the home page
    When I add a product to cart
    And I click cart icon to go on cart page
    Then I should be redirected to the cart page

  Scenario: Successful adding the product to cart and complete the checkout process
    When I click on checkout button
    Then Enter your information page should be shown and information will be filled
    And I click on continue button on information page
    Then Information overview page will be shown
    When I click on finish button on information overview page
    Then order should get placed successfully
