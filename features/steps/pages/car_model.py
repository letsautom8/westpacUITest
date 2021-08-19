from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CarModel:
    VOTE_COUNT = (By.XPATH, '//my-model//h4[contains(text(),\'Votes\')]//strong')
    VOTE_BUTTON = (By.XPATH, '//my-model//button[text()=\'Vote!\']')
    THANK_YOU_TEXT = (By.XPATH, '//my-model//p[contains(text(),\'Thank you\')]')

    def __init__(self, browser):
        self.browser = browser
        self.current_vote = self.get_vote_count()

    def cast_vote(self):
        self.browser.find_element(*self.VOTE_BUTTON).click()
        self.browser.find_element(*self.THANK_YOU_TEXT)

    def get_vote_count(self):
        return int(self.browser.find_element(*self.VOTE_COUNT).text)
