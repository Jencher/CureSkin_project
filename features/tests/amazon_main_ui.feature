# Created by aleksandrkryzhanovskii at 5/15/23
Feature: Tests for main page UI

  Scenario: User sees all footer links
    Given Open amazon main page
    Then Verify there are 36 links
