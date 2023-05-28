# Created by aleksandrkryzhanovskii at 5/22/23
Feature: Tests for Google

  Scenario Outline: User can search for product in Google
    Given Open Google main page
    When  Input <search_word> into Google search field
    And Click Google Search button
    Then Verify Page URL has <search_result> in it
  Examples:
    |search_word      |search_result  |
    |plate            |plate          |
    |mug              |mug            |
    |cup              |cup            |