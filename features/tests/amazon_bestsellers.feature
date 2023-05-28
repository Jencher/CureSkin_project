# Created by aleksandrkryzhanovskii at 5/15/23
Feature: Test for bestsellers functionality


  Scenario: There are 5 bestsellers links
    Given Open Amazon Bestsellers
    Then Verify there are 5 top links

  Scenario: Bestsellers links can be opened
    Given Open Amazon Bestsellers
    Then User can click through top links and verify correct page opens
