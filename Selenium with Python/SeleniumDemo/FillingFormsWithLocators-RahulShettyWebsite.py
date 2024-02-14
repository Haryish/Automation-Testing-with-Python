from selenium import webdriver
# from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Drive - ChromeBrowser
serviceObj = Service()  # selenium webservice Manager / seleniumManager
driver = webdriver.Chrome(service=serviceObj)

sourceurl = 'https://rahulshettyacademy.com/angularpractice/'



driver.maximize_window()
driver.get(sourceurl)

driver.implicitly_wait(10)

