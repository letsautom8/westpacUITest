### 1. Setup requirements 
1. python 3.9 or above
2. docker
3. docker-compose
4. Shell terminal (Linux or Linux compatible)

### 2. Recommendations
If you are using a mac, it is recommended to create a virtual workspace for the project. This way, the default system python will not be affected by the libraries being installed
 1. On you terminal run the following  
```
python3 -m pip install --user virtualenv
```

2. Create a virtual environment
```
python3 -m venv env
```

3. Activate the workspace
``` 
source env/bin/activate
```

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Setup your local selenium hub and chrome

    docker-compose up -d

> #### Note
> The advantage of this dockerised hub and chrome to execute the test is it is portable due to it being supported by docker
> 
> The selenium hub docker exposes port 4444 by default
### 5. Running the tests 

    behave


Sample output:
```buildoutcfg
Feature: As a user, I should be able to login to start rating cars # features/login.feature:1

  Scenario: Verify Login and Logout for existing user  # features/login.feature:3
    Given I am a user with valid credentials           # features/steps/steps.py:13 0.000s
    When I go to buggy cars rating homepage            # features/steps/steps.py:18 0.893s
    And I login with current username and password     # features/steps/steps.py:24 0.297s
    Then I should be able to login                     # features/steps/steps.py:29 0.138s
    And I should be able to logout                     # features/steps/steps.py:33 5.138s

Feature: As a user, I should be able to check navigation on the site # features/navigation.feature:1

  Scenario: Verify navigation is working         # features/navigation.feature:3
    Given I am a user with valid credentials     # features/steps/steps.py:13 0.000s
    When I go to buggy cars rating homepage      # features/steps/steps.py:18 0.357s
    And I click on Overall Rating                # features/steps/steps.py:58 0.102s
    Then Overall Rating page should be displayed # features/steps/steps.py:63 0.649s

Feature: As a user, I should be able to login to start rating cars # features/profile.feature:1

  Scenario: Verify Profile update                   # features/profile.feature:4
    Given I generate a new valid user credential    # features/steps/steps.py:38 0.000s
    When I go to buggy cars rating homepage         # features/steps/steps.py:18 0.333s
    And I register my new credential                # features/steps/steps.py:43 0.863s
    When I login with current username and password # features/steps/steps.py:24 0.284s
    And I go to buggy cars rating homepage          # features/steps/steps.py:18 0.300s
    And I go to my profile page                     # features/steps/steps.py:85 0.141s
    And I update my password                        # features/steps/steps.py:90 0.525s
    And I logout                                    # features/steps/steps.py:98 0.081s
    And I login with current username and password  # features/steps/steps.py:24 0.249s
    Then I should be able to login                  # features/steps/steps.py:29 0.015s
    And I should be able to logout                  # features/steps/steps.py:33 5.113s

Feature: As a new user, I should be able to register to start rating cars # features/register.feature:1

  Scenario: Verify user can register successfully   # features/register.feature:3
    Given I generate a new valid user credential    # features/steps/steps.py:38 0.000s
    When I go to buggy cars rating homepage         # features/steps/steps.py:18 0.297s
    And I register my new credential                # features/steps/steps.py:43 0.871s
    Then there is no error message                  # features/steps/steps.py:54 5.058s
    When I login with current username and password # features/steps/steps.py:24 0.257s
    Then I should be able to login                  # features/steps/steps.py:29 0.071s
    And I should be able to logout                  # features/steps/steps.py:33 5.087s

Feature: As a new user, I should be able to vote my favourite car # features/voting.feature:1

  Scenario: Verify vote is working                 # features/voting.feature:3
    Given I generate a new valid user credential   # features/steps/steps.py:38 0.000s
    When I go to buggy cars rating homepage        # features/steps/steps.py:18 0.290s
    And I register my new credential               # features/steps/steps.py:43 0.816s
    And I go to buggy cars rating homepage         # features/steps/steps.py:18 0.296s
    And I login with current username and password # features/steps/steps.py:24 0.252s
    And I click on Overall Rating                  # features/steps/steps.py:58 0.114s
    And I select the top car                       # features/steps/steps.py:67 2.421s
    And I casted my vote                           # features/steps/steps.py:72 1.568s
    Then vote should be successful                 # features/steps/steps.py:76 0.031s
    And I should be able to logout                 # features/steps/steps.py:33 5.140s

5 features passed, 0 failed, 0 skipped
5 scenarios passed, 0 failed, 0 skipped
37 steps passed, 0 fail
```
### 6. Viewing the execution
The execution runs on docker environment.
The VNC port is exposed so the execution can be inspected.
To view it, download and vnc client and connect to port `49338`

For example: vnc://localhost:49338

### 7. Test Approach
[Test Approach can be found here](https://github.com/letsautom8/westpacUITest/blob/main/testapproach.md)

### 8. Bug Report
[Bug Report can be found here](https://github.com/letsautom8/westpacUITest/blob/main/Buggy%20Cars%20Rating%20Bugs.docx)