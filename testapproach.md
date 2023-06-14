## Test Documentation

## 1. Test approach
The website aims to display different car models and their ratings based on total votes of user.
It also provides mechanism for users to create their profile, manage profile, vote and leave comments.

With this in mind, the test approach revolves on testing the  purpose of the website and the components that makes up the website namely front end and backend.

1. Verify the requests (not automated). Some of them are
   Login:
   
```buildoutcfg
    https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/oauth/token
```
   Get Current user:
```buildoutcfg
    https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/users/current
```
    
Query:
```buildoutcfg
    https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/models?page=1
    https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/models?page=1&orderBy=rank
```

2. Verify the UI Functionality(automated)
   Verification of UI functionality ensures that the views are updated properly since it is the UI that is facing the user.
   Testing involves:
    - Session management - checks whether user can login and logout
    - Profile management - checks whether user can manage their profiles
    - Vote functionality
    - Navigation checks
    - Filter checks

#### Bugs
Bugs are documented in this [file](https://github.com/letsautom8/westpacUITest/blob/main/Buggy%20Cars%20Rating%20Bugs.docx).

### Automation setup
Automation setup is documented [here](https://github.com/letsautom8/westpacUITest/blob/main/readme.md)
#### Further enhancements
- **API automation**: This will ensure that the api's are working properly before moving to the UI tests and they are fairly quick to execute than UI tests.
- **Reporting**: via Email or upload via CI/CD
- **CI/CD**: We can add this component to execute the tests automatically whenever there are updates to the site.


