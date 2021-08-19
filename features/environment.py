from time import sleep

from selenium import webdriver
from features.model.user import User

def before_all(context):
	desired_capabilities = webdriver.DesiredCapabilities.CHROME
	desired_capabilities['browserName'] = 'chrome'

	context.browser = webdriver.Remote(
		desired_capabilities=desired_capabilities,
		command_executor="http://localhost:4444/wd/hub"
	)
	context.browser.implicitly_wait(5)
	context.user = User()

def after_step(context,step):
	sleep(0.5)
def after_all(context):
	context.browser.quit()