from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome Drive - ChromeBrowser
serviceObj = Service()  # selenium webservice Manager / seleniumManager
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
