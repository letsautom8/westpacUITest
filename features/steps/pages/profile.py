from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Profile:
    USERNAME_INPUT = (By.NAME, 'username')
    FIRST_NAME_INPUT = (By.NAME, 'firstName')
    LAST_NAME_INPUT = (By.NAME, 'lastName')
    CURRENT_PASSWORD_INPUT = (By.ID, 'currentPassword')
    NEW_PASSWORD_INPUT = (By.ID, 'newPassword')
    NEW_PASSWORD_CONFIRM_INPUT = (By.ID, 'newPasswordConfirmation')
    ERROR_MESSAGE = (By.CSS_SELECTOR,'div.result.alert.alert-danger')
    SAVE_BUTTON = (By.XPATH, '//button[text()=\'Save\']')

    def __init__(self, browser):
        self.browser = browser
        self.register = None

    def set_firstname(self, firstname):
        elem = self.browser.find_element(*self.FIRST_NAME_INPUT)
        elem.clear()
        elem.send_keys(firstname + Keys.RETURN)

    def get_phone_number(self):
        elem = self.browser.find_element(*self.FIRST_NAME_INPUT)
        return elem.text

    def set_lastname(self, lastname):
        elem = self.browser.find_element(*self.LAST_NAME_INPUT)
        elem.clear()
        elem.send_keys(lastname + Keys.RETURN)

    def set_current_password(self, text):
        elem = self.browser.find_element(*self.CURRENT_PASSWORD_INPUT)
        elem.clear()
        elem.send_keys(text + Keys.RETURN)

    def set_new_password(self, text):
        elem = self.browser.find_element(*self.NEW_PASSWORD_INPUT)
        elem.clear()
        elem.send_keys(text + Keys.RETURN)

    def set_confirm_password(self, text):
        elem = self.browser.find_element(*self.NEW_PASSWORD_CONFIRM_INPUT)
        elem.clear()
        elem.send_keys(text + Keys.RETURN)

    def get_error_message(self):
        try:
            msg = self.browser.find_element(*self.ERROR_MESSAGE).text
            return msg
        except:
            return None

    def click_save(self):
        self.browser.find_element(*self.SAVE_BUTTON).click()
