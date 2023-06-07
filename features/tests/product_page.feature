# Created by aleksandrkryzhanovskii at 5/15/23
Feature: Amazon Add Item test

  Scenario: User can add a product to the cart
   Given Open Amazon main page
   When Search for Plate
   And Click on the first product
   And Click on Add to cart button
   And Close Banner
   Then Verify cart has 1 item
   Then Verify cart has Plate
