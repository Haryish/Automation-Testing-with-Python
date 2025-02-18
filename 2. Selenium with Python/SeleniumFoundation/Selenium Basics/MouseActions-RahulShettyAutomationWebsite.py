from selenium import webdriver
from selenium.webdriver import ActionChains
# from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Drive - ChromeBrowser
serviceObj = Service()  # selenium webservice Manager / seleniumManager
driver = webdriver.Chrome(service=serviceObj)

sourceurl = 'https://rahulshettyacademy.com/AutomationPractice/'

driver.maximize_window()
driver.get(sourceurl)

driver.implicitly_wait(2)

action = ActionChains(driver)
action.scroll_to_element(driver.find_element(By.CLASS_NAME, "mouse-hover")).perform()

driver.implicitly_wait(2)

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

driver.implicitly_wait(2)

driver.close()
