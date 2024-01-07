Feature: Register Account Functionality

  Background: common steps
    Given I navigate to Register Page

  Scenario: Register with mandatory fields
    When I enter below details into mandatory fields
        |first_name|last_name|
        |chandra   |sekhar   |
    And I select Privacy Policy option
    And I click on Continue button
    Then Account should get created

  Scenario: Register with all fields
    When I enter below details into all fields
         |first_name|last_name|
         |chandra   |sekhar   |
    And I select Privacy Policy option
    And I click on Continue button
    Then Account should get created

  Scenario: Register with a duplicate email address
    When I enter below details into all fields except email field
         |first_name|last_name|
         |chandra   |sekhar   |
    And I enter existing accounts email into email field
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper warning message information about duplicate account should be displayed

  Scenario: Register without providing any details
    When I dont enter anything into the fields
    And I click on Continue button
    Then Proper warning message for every mandatory fields should be displayed

