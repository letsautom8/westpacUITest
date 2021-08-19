Feature: As a new user, I should be able to vote my favourite car

Scenario: Verify vote is working
	Given I generate a new valid user credential
	When I go to buggy cars rating homepage
		And I register my new credential
		And I go to buggy cars rating homepage
		And I login with current username and password
		And I click on Overall Rating
		And I select the top car
		And I casted my vote
	Then vote should be successful
		And I should be able to logout
