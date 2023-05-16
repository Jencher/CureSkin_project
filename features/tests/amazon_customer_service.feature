# Created by aleksandrkryzhanovskii at 5/15/23
Feature: Amazon Customer Service Tests


  Scenario: UI elements are presented on the page
    Given Open Amazon Customer Service page
    Then Verify Welcome text is visible
    Then Verify 10 help boxes are displayed
    Then Verify Search our help library text is visible
    Then Verify search help input is presented
    Then Verify All help topics text is visible
    Then Verify help topics menu is presented
