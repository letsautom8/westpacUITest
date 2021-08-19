Feature: As a user, I should be able to login to start rating cars

Scenario: Verify Login and Logout for existing user
	Given I am a user with valid credentials
	When I go to buggy cars rating homepage
		And I login with current username and password
	Then I should be able to login
		And I should be able to logout
