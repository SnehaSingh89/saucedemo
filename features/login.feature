Feature: Login functionality of SauceDemo

  Scenario: Successful logout with valid credentials
    Given the user is on the logout page
    And user enters submit button
    When the user logs in with username "standard_user" and password "secret_sauce"
    Then the user should be redirected to the products page
    And the user should see the product list

    Scenario: Unsuccessful login with invalid credentials
      Given the user is on the login page
        When the user logs in with username "invalid_user" and password "wrong_password"
        Then the user should see an error message "Epic sadface: Username and password do not match any user in this service"
        Then the user is on the login page