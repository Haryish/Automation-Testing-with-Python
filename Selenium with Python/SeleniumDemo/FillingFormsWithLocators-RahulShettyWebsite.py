import time

from selenium import webdriver
# from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait

# Chrome Drive - ChromeBrowser
serviceObj = Service()  # selenium webservice Manager / seleniumManager
driver = webdriver.Chrome(service=serviceObj)

sourceurl = 'https://rahulshettyacademy.com/angularpractice/'

driver.maximize_window()
driver.get(sourceurl)

time.sleep(10)

driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("Haryish Elangumaran")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("haryishkumaran16@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
dropdown = Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
dropdown.select_by_index(1)
driver.find_element(By.XPATH, "//input[@name='bday']").send_keys("03101999")

time.sleep(5)

driver.find_element(By.XPATH, "//input[@type='submit']").click()

# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.visibility_of_element_located(By.CLASS_NAME("alert-success")))

time.sleep(5)

print(driver.find_element(By.CLASS_NAME, "alert-success").text)

time.sleep(5)

driver.close()
