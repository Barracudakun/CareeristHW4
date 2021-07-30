Feature: Test Amazon cart

  Scenario: Test the numbers of items into the cart
    Given Open amazon page
    When Search for shoes
    And Click on the first product
    And Click on Add to cart button
    Then Verify cart has 1 item


  Scenario: User sees empty shopping cart
    Given Open amazon page
    When Click on cart icon
    Then "Your Amazon Cart is empty" message is displayed