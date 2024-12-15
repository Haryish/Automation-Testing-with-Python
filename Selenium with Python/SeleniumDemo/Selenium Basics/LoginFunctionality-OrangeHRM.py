from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Drive - ChromeBrowser
serviceObj = Service()  # selenium webservice Manager / seleniumManager
driver = webdriver.Chrome(service=serviceObj)

sourceurl = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

driver.maximize_window()
driver.get(sourceurl)

driver.implicitly_wait(10)

driver.find_element(By.NAME, "username").send_keys("Admin")

driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//div/input[@placeholder='Password']").send_keys("admin123")


# Wait for the login button to be clickable and then click
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]")))
login_button.click()

# Wait for the dashboard to be visible after logging in
WebDriverWait(driver, 10).until(EC.url_to_be('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'))

print(driver.title)

# Assert the URL
assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

# Close the browser
driver.close()