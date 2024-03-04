import time

from selenium import webdriver
# from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    # Chrome Drive - ChromeBrowser
    serviceObj = Service()  # selenium webservice Manager / seleniumManager
    driver = webdriver.Chrome(service=serviceObj)

    sourceUrl = 'https://rahulshettyacademy.com/loginpagePractise/'

    driver.maximize_window()
    driver.get(sourceUrl)

    driver.implicitly_wait(5)

    driver.close()