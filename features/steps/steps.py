from features.model.user import User
from features.steps.pages.car_model import CarModel
from features.steps.pages.home import Home
from features.steps.pages.overall_ratings import OverallRatings
from features.steps.pages.profile import Profile
from pages.navigation import Navigation
from hamcrest import *
from time import sleep
import random
import string


@given('I am a user with valid credentials')
def step(context):
    context.user.username = 'Kukzee168'
    context.user.password = 'Broodling@168'

@given('I go to buggy cars rating homepage')
@when('I go to buggy cars rating homepage')
def step(context):
    context.browser.get('http://buggy.justtestit.org/')
    context.home = Home(context.browser)

@when('I login with current username and password')
def step(context):
    context.navigation = Navigation(context.browser)
    context.navigation.login(context.user.username, context.user.password)

@then('I should be able to login')
def step(context):
    assert_that(context.navigation.get_state(), equal_to(True), "User not logged in")

@then('I should be able to logout')
def step(context):
    context.navigation.logout()
    assert_that(context.navigation.get_state(), equal_to(False), "User still logged in")

@given('I generate a new valid user credential')
def step(context):
    context.user = User()
    context.user.valid()

@when('I register my new credential')
def step(context):
    context.navigation = Navigation(context.browser)
    context.register = context.navigation.click_register()
    context.register.set_username(context.user.username)
    context.register.set_firstname(context.user.firstname)
    context.register.set_lastname(context.user.lastname)
    context.register.set_password(context.user.password)
    context.register.set_confirm_password(context.user.password)
    context.register.click_register()

@then(u'there is no error message')
def step(context):
    assert_that(context.register.get_error_message(), equal_to(None), "Error message present")

@when(u'I click on Overall Rating')
def step_impl(context):
    context.home.click_overall_ratings()
    context.overall_ratings = OverallRatings(context.browser)

@then(u'Overall Rating page should be displayed')
def step_impl(context):
    assert_that(context.overall_ratings.is_loaded(), equal_to(True), "Overall ratings not loaded")

@when(u'I select the top car')
def step_impl(context):
    context.overall_ratings.select_top_car()
    context.car_model = CarModel(context.browser)

@when(u'I casted my vote')
def step_impl(context):
    context.car_model.cast_vote()

@then(u'vote should be successful')
def step_impl(context):
    assert_that(context.car_model.get_vote_count(), equal_to(context.car_model.current_vote + 1),
                "Vote not counted")

@when(u'I waited')
def step_impl(context):
    sleep(10)

@when(u'I go to my profile page')
def step_impl(context):
    context.navigation.click_profile()
    context.profile = Profile(context.browser)

@when(u'I update my password')
def step_impl(context):
    context.profile.set_current_password(context.user.password)
    context.user.change_password()
    context.profile.set_new_password(context.user.password)
    context.profile.set_confirm_password(context.user.password)
    context.profile.click_save()

@when(u'I logout')
def step_impl(context):
    context.navigation.logout()

