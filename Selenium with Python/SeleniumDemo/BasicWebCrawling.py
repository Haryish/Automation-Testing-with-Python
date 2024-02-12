from selenium import webdriver
# from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Drive - ChromeBrowser
serviceObj = Service()  # selenium webservice Manager / seleniumManager
driver = webdriver.Chrome(service=serviceObj)

sourceurl = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

driver.maximize_window()
driver.get(sourceurl)

driver.implicitly_wait(10)

driver.find_element(By.NAME, "username").send_keys("Admin")

driver.implicitly_wait(5)
driver.find_element(By.XPATH,
                    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div["
                    "2]/input[1]").send_keys(
    "admin123")

driver.implicitly_wait(5)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div["
                              "3]/button[1]").click()


driver.implicitly_wait(10)

print(driver.title)
driver.implicitly_wait(20)

driver.close()
