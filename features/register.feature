Feature: As a new user, I should be able to register to start rating cars

Scenario: Verify user can register successfully
	Given I generate a new valid user credential
	When I go to buggy cars rating homepage
		And I register my new credential
	Then there is no error message
	When I login with current username and password
	Then I should be able to login
		And I should be able to logout

