# Created by aleksandrkryzhanovskii at 5/7/23
Feature: Amazon Search tests

  Scenario: User can search for table on Amazon
    Given Open Amazon main page
    When Search for table
    Then Verify search results shown for "table"

  Scenario: User can search for coffee on Amazon
  Scenario Outline: User can search on Amazon
    Given Open Amazon main page
    When Search for coffee
    Then Verify search results shown for "coffee"
    When Search for <search_word>
    Then Verify search results shown for <search_result>
    Examples:
    |search_word      |search_result    |
    |table            |"table"          |
    |coffee           |"coffee"         |
    |mug              |"mug"            |
    |dress            |"dress"          |

