# Created by aleksandrkryzhanovskii at 5/7/23
Feature: Amazon Sign-in tests


  Scenario: Sign-in page is visible and email field presented
    Given Open Amazon main page
    When Click Orders
    Then Verify Sign In page opens
    Then Verify sign-in text is visible
    Then Verify email field is presented

  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon main page
    When Click on button from SignIn popup
    Then Verify Sign In page opens

   Scenario: Amazon users see sign in button
     Given Open amazon main page
     Then Verify Sign In is clickable
     When Wait for 3 sec
     Then Verify Sign In is clickable
     Then Verify Sign In disappears