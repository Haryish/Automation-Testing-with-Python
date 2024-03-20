import time

from selenium import webdriver
# from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Drive - ChromeBrowser
serviceObj = Service()  # selenium webservice Manager / seleniumManager
driver = webdriver.Chrome(service=serviceObj)

chrome_option = webdriver.ChromeOptions()

chrome_option.add_argument("--start-maximized")

url1 = "https://rahulshettyacademy.com/seleniumPractise/#/"

time.sleep(2)

driver.get(url1)

driver.find_element(By.LINK_TEXT, "Top Deals").click()

wh = driver.window_handles

driver.switch_to.window(wh[1])

driver.find_element(By.XPATH, "//input[@id='search-field']").send_keys("b")

items = []

elements = driver.find_elements(By.XPATH, "//td[1]")

for element in elements:
    item = element.text
    items.append(item)

print("Initial List: ", items)

manual_sort = sorted(items)

driver.find_element(By.XPATH, "//span[@class='sort-icon sort-descending']").click()

a_items = []

elements = driver.find_elements(By.XPATH, "//td[1]")

for element in elements:
    a_item = element.text
    a_items.append(a_item)

actual_sort = a_items

print("Sorted Items (via web): ", a_items)

assert manual_sort == actual_sort

time.sleep(2)

driver.close()
