from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.steps.pages.register import Register


class Navigation:
    USERNAME_INPUT = (By.NAME, 'login')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[text()=\'Login\']')
    PROFILE_LINK = (By.XPATH, '//nav//my-login//a[@href=\'/profile\']')
    REGISTER_LINK =( By.XPATH, '//nav//my-login//a[@href=\'/register\']')
    LOGOUT_LINK = (By.XPATH, '//nav//my-login//a[text()=\'Logout\']')

    def __init__(self, browser):
        self.browser = browser
        self.register = None
    
    def set_username(self, username):
        search_input = self.browser.find_element(*self.USERNAME_INPUT)
        search_input.send_keys(username + Keys.RETURN)
    
    def set_password(self, password):
        search_input = self.browser.find_element(*self.PASSWORD_INPUT)
        search_input.send_keys(password + Keys.RETURN)

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def click_register(self):
        self.browser.find_element(*self.REGISTER_LINK).click()
        return Register(self.browser)

    def click_profile(self):
        self.browser.find_element(*self.PROFILE_LINK).click()

    def logout(self):
        self.browser.find_element(*self.LOGOUT_LINK).click()

    def get_state(self):
        try:
            self.browser.find_element(*self.PROFILE_LINK)
            return True
        except:
            return False

