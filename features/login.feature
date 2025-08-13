Feature: Login functionality of SauceDemo

  Scenario: Successful login with valid credentials
    Given  user is on the login page
    When user logs in with username "standard_user" and password "secret_sauce"
    Then  user should be redirected to the products page
