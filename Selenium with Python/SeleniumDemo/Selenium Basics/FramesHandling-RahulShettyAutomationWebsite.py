from selenium import webdriver
# from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Drive - ChromeBrowser
serviceObj = Service()  # selenium webservice Manager / seleniumManager
driver = webdriver.Chrome(service=serviceObj)

url1 = "https://rahulshettyacademy.com/AutomationPractice/"

driver.maximize_window()

driver.get(url1)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

driver.switch_to.frame("courses-iframe")

getText = driver.find_element(By.XPATH, "//div[@class='col-md-6 text-left']//h2").text

print(getText)

driver.switch_to.default_content()

driver.execute_script("window.scrollBy(document.body.scrollHeight,0)")

driver.quit()
