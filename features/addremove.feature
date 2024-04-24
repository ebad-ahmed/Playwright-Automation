Feature: Add and Remove product from cart
  As a standard user
  I want to be able to add product to the and then remove that product from cart

  Scenario: Successful Adding and Removing
    Given I am on the home page
    When I add a product to cart
    And I click cart icon to go on cart page
    Then I should be redirected to the cart page
    When I click on remove button on cart page
    Then product should be removed

