import time

# from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass


# from selenium.webdriver.support.wait import WebDriverWait


# @pytest.mark.usefixtures("setup")
class TestMiniCase(BaseClass):

    def testCaseOne(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("Haryish Elangumaran")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("haryishkumaran16@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
        dropdown = Select(self.driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
        dropdown.select_by_index(1)
        self.driver.find_element(By.XPATH, "//input[@name='bday']").send_keys("03101999")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
