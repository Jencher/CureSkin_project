# Created by aleksandrkryzhanovskii at 5/7/23
Feature: Amazon Sign-in tests


  Scenario: Sign-in page is visible and email field presented
    Given Open Amazon main page
    When Click Orders
    Then Verify sign-in text is visible
    Then Verify email field is presented