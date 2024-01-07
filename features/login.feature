Feature: Login Functionality

  Background: common steps
    Given I navigated to Login Page

  Scenario: Login with valid credentials
    When I enter valid email address say "chandra1234@gmail.com" and valid password say "chandu" into the fields
    And I click on Login button
    Then I should get logged in

  Scenario: Login with invalid email and valid password
    When I enter invalid email and valid password say "chandu" into the fields
    And I click on Login button
    Then I should get a proper warning message

  Scenario: Login with valid email and invalid password
    When I enter valid email say "chandra1234@gmail.com" and invalid password say "chandu123" into the fields
    And I click on Login button
    Then I should get a proper warning message


  Scenario: Login with invalid credentials
    When I entered invalid email and invalid password say "chandu123" into the fields
    And  I click on Login button
    Then I should get a proper warning message

  Scenario: Login without entering any credentials
    When  I dont enter anything into email and password fields
    And I click on Login button
    Then I should get a proper warning message
