Feature: As a user, I should be able to login to start rating cars

Scenario: Verify Profile update
	Given I generate a new valid user credential
	When I go to buggy cars rating homepage
		And I register my new credential
	When I login with current username and password
		And I go to buggy cars rating homepage
		And I go to my profile page
		And I update my password
		And I logout
		And I login with current username and password
	Then I should be able to login
		And I should be able to logout
