from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Register:
    USERNAME_INPUT = (By.NAME, 'username')
    FIRST_NAME_INPUT = (By.NAME, 'firstName')
    LAST_NAME_INPUT = (By.NAME, 'lastName')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#password')
    PASSWORD_CONFIRM_INPUT = (By.NAME, 'confirmPassword')
    ERROR_MESSAGE = (By.CSS_SELECTOR,'div.result.alert.alert-danger')
    REGISTER_BUTTON = (By.XPATH, '//button[text()=\'Register\']')

    def __init__(self, browser):
        self.browser = browser
        self.register = None

    def set_username(self, username):
        search_input = self.browser.find_element(*self.USERNAME_INPUT)
        search_input.clear()
        search_input.send_keys(username + Keys.RETURN)

    def set_firstname(self, firstname):
        search_input = self.browser.find_element(*self.FIRST_NAME_INPUT)
        search_input.clear()
        search_input.send_keys(firstname + Keys.RETURN)
    
    def set_lastname(self, lastname):
        search_input = self.browser.find_element(*self.LAST_NAME_INPUT)
        search_input.clear()
        search_input.send_keys(lastname + Keys.RETURN)

    def set_password(self, text):
        search_input = self.browser.find_element(*self.PASSWORD_INPUT)
        search_input.clear()
        search_input.send_keys(text + Keys.RETURN)

    def set_confirm_password(self, text):
        search_input = self.browser.find_element(*self.PASSWORD_CONFIRM_INPUT)
        search_input.clear()
        search_input.send_keys(text + Keys.RETURN)

    def get_error_message(self):
        try:
            msg = self.browser.find_element(*self.ERROR_MESSAGE).text
            return msg
        except:
            return None

    def click_register(self):
        self.browser.find_element(*self.REGISTER_BUTTON).click()
