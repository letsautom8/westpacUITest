from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Home:
    OVERALL_RATINGS_CARD = (By.XPATH, '//div[@class=\'container\']//div[3]//a')

    def __init__(self, browser):
        self.browser = browser

    def click_overall_ratings(self):
        elem = self.browser.find_element(*self.OVERALL_RATINGS_CARD)
        elem.click()
