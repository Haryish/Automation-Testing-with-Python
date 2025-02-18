import time

from selenium import webdriver
# from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    # Chrome Drive - ChromeBrowser
    serviceObj = Service()  # selenium webservice Manager / seleniumManager
    driver = webdriver.Chrome(service=serviceObj)

    sourceurl = 'https://rahulshettyacademy.com/AutomationPractice/'

    driver.maximize_window()
    driver.get(sourceurl)

    driver.implicitly_wait(5)

    driver.find_element(By.ID, "openwindow").click()
    driver.find_element(By.ID, "opentab").click()

    time.sleep(10)

    i = 0
    wh = driver.window_handles

    for window in wh:
        driver.switch_to.window(window)
        print("Title of Window ID: ", window, "is", driver.title)
        driver.switch_to.window(wh[0])



    driver.quit()
