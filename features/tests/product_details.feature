# Created by aleksandrkryzhanovskii at 5/25/23
Feature: Tests for product page

  Scenario: User can select colors
    Given Open Amazon product B081YS2F7N page
    Then Verify user can click through colors


  Scenario: User can select dress colors
    Given Open Amazon product B07JN9JTD9 page
    Then Verify user can click through colors


  Scenario:  User can see the deals
    Given Open Amazon product B074TBCSC8 page
    When Hover over New arrivals
    Then User can see the deals