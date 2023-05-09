# Created by aleksandrkryzhanovskii at 5/9/23
Feature: Tests for Amazon Shopping Cart


  Scenario: User can verify  that shopping cart is empty
    Given Open Amazon main page
    When Click on Cart icon
    Then Verify Your Amazon Cart is empty