from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OverallRatings:
    def __init__(self, browser):
        self.browser = browser

    def is_loaded(self):
        try:
            WebDriverWait(self.browser, 2).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'table.cars'))
                )
            return True
        except:
            return False

    def select_top_car(self):
        elem =WebDriverWait(self.browser, 3).until(
                EC.presence_of_element_located((By.XPATH, '//my-overall//tr[1]/td[1]/a'))
            )
        elem.click()
