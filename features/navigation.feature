Feature: As a user, I should be able to check navigation on the site

Scenario: Verify navigation is working
	Given I am a user with valid credentials
	When I go to buggy cars rating homepage
	And I click on Overall Rating
	Then Overall Rating page should be displayed