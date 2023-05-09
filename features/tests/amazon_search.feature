# Created by aleksandrkryzhanovskii at 5/7/23
Feature: Amazon Search tests

  Scenario: User can search for table on Amazon
    Given Open Amazon main page
    When Search for table
    Then Verify search results shown for "table"

  Scenario: User can search for coffee on Amazon
    Given Open Amazon main page
    When Search for coffee
    Then Verify search results shown for "coffee"

