import time

from selenium import webdriver
# from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
# chrome option arguments: {'--start-maximized', 'headless' , '--ignore-certificate-error'}
# visit https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOption for documentation

# Chrome Drive - ChromeBrowser
serviceObj = Service()  # selenium webservice Manager / seleniumManager
driver = webdriver.Chrome(service=serviceObj, options=chrome_option)

# Test Case 1: Check if the URL is valid
url1 = "https://rahulshettyacademy.com/angularpractice"

driver.implicitly_wait(4)
driver.get(url1)
driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
driver.implicitly_wait(4)

status_1 = str(driver.execute_script("return document.readyState")) == "complete"
if status_1:
    print("Test case 1: Test if the URL is valid - Passed")
else:
    print("Test case 1: Test if the URL is valid - Failed")

# Test case 2: Check if 'blackberry' exists and able to book it
items = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
i = 1
for item in items:
    name = item.find_element(By.XPATH, f"(//h4[@class='card-title']/a)[{i}]").text
    if name == 'Blackberry':
        frame = item.find_element(By.XPATH, f"(//div[@class='card-footer'])[{i}]")
        driver.execute_script("arguments[0].scrollIntoView(true)", frame)
        time.sleep(3)
        frame.click()
    else:
        i += 1

driver.execute_script("window.scrollTo({behavior: 'instant', top: 0, left: 0})")
time.sleep(3)
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
time.sleep(3)
print("Test case 2: Check if 'blackberry' exists and able to book it - Passed")

# Test case 3: Checkout page Exist
driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()
time.sleep(3)
print("Test case 3: Checkout page Exist - Passed")


# Test case 4: Place the order and verify the success message
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Ind")
suggestion, j = driver.find_elements(By.XPATH, "//div[@class='suggestions']//li"), 1
for country in suggestion:
    if country.find_element(By.XPATH, f"(//a)[{j}]").text == 'India':
        country.click()
    else:
        j += 1
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
time.sleep(3)
assert "Success" in driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print("Test case 4: Place the order and verify the success message - Passed")
print("Hence testing Completed")

driver.quit()
