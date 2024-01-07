Feature: Search Functionality

  Background: common steps
    Given Navigated to Home Page

  Scenario: Search for a valid product
    When Enter valid product say "HP" into the Search box field
    And Click on Search button
    Then valid product should get displayed in Search results

  Scenario: Search for an invalid product
    When Enter invalid product say "Honda" into the Search box field
    And Click on Search button
    Then proper message should be displayed in Search results

  Scenario: Search Without entering any product
    When dont enter anything into Search box field
    And Click on Search button
    Then Proper message should be displayed in search results