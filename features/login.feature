Feature: Login functionality of SauceDemo

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user logs in with username "standard_user" and password "secret_sauce"
    Then the user should be redirected to the products page
    And the user should see the product list

    Scenario: Unsuccessful login with invalid credentials
      Given the user is on the login page
