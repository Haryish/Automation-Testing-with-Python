from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service

# Chrome Drive - ChromeBrowser
browser = input("Input the Browser for execution: ")
serviceObj = Service()  # selenium webservice Manager / seleniumManager

try:
    if browser == 'Chrome':
        driver = webdriver.Chrome(service=serviceObj)

    elif browser == 'Firefox':
        driver = webdriver.Firefox(service=serviceObj)

    elif browser == 'Edge':
        driver = webdriver.Edge(service=serviceObj)
    else:
        print("invalid browser name")

except WebDriverException:
    raise "WebDriver/Browser is not set"
finally:
    print("Running on default browser")
    driver = webdriver.Chrome(service=serviceObj)

url1 = "https://cognizant.udemy.com"

driver.minimize_window()

driver.get(url1)

print("Webpage : ", url1)
print("Title of the webpage : ", driver.title)

url2 = "https://be.cognizant.com"

driver.get(url2)
driver.maximize_window()
driver.back()
driver.refresh()
driver.forward()

driver.close()
