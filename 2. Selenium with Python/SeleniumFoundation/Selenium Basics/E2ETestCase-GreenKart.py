"""Preparation of End-to-End test scenario that uses 'https://rahulshettyacademy.com/seleniumPractise/#/' as a base
url.

 Search with any 3 characters - Get the name of vegetables into a list and then validate it with the search
input to check if the search results are correct or not. Add All Items to the cart and then click the kart button,
this opens the Checkout page. Fetch the price of each item to a list and then add them, similarly fetch the value of
sum and validate the Apply coupon code 'rahulshettyacademy' and check discount by fetching the value and then
asserting them with hardcoded value calculate the discounted value and feed them as expected value. Finally, compare
the discounted value with the "total after discount" field. """
import time

from selenium import webdriver
# from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


# from selenium.webdriver.support.wait import WebDriverWait

def searchAnalysis(wordlist, search):
    result = True
    for word in wordlist:
        if search in word.text:
            break
            # print("The Item Name: " + word.text + " has characters '" + search+"'")
        else:
            result = False
            # print("The Item Name: " + word.text + " does not have " + search)
    return result


def convey(buffer):
    if buffer:
        return "Passed"
    else:
        return "Failed"


def displayCase(testcase, buffer):
    print(testcase + " - " + str(convey(buffer)))


def manual_sum(amountList):
    add = 0
    for price in amountList:
        add = add + int(price)
    return add


def scenarioStatus(testStatus):
    y = True
    for test in testStatus:
        y = y & test

    return convey(y)


if __name__ == "__main__":

    status = []

    # Chrome Drive - ChromeBrowser
    serviceObj = Service()  # selenium webservice Manager / seleniumManager
    driver = webdriver.Chrome(service=serviceObj)

    baseUrl = 'https://rahulshettyacademy.com/seleniumPractise/#/'

    driver.maximize_window()
    driver.get(baseUrl)

    time.sleep(2)

    searchInput = "ber"

    driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys(searchInput)
    driver.find_element(By.CLASS_NAME, "search-button").click()
    resultant = driver.find_elements(By.XPATH, "//h4[@class='product-name']")
    status.append(searchAnalysis(resultant, searchInput))

    displayCase("Test Case 1: Verify if the resultant items has retrieved based on search input", status[0])

    addToKart = driver.find_elements(By.XPATH, "//div[@class='product-action']//button")
    for items in addToKart:
        items.click()
    driver.implicitly_wait(6)
    driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
    driver.implicitly_wait(6)
    driver.find_element(By.CSS_SELECTOR, "div[class='cart-preview active'] button[type='button']").click()
    time.sleep(5)

    status.append(driver.find_element(By.XPATH, '//thead//td[1]').is_displayed())

    displayCase("Test Case 2: Test on navigability to Checkout page", status[1])

    eachItem = driver.find_elements(By.XPATH, "//td[5]//p[@class='amount']")

    prices = []
    for amount in eachItem:
        prices.append(amount.text)

    actual_sum = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
    expected_sum = manual_sum(prices)
    status.append(actual_sum == expected_sum)

    displayCase("Test Case 3: Verify the sum of item displayed in webpage", status[2])

    driver.find_element(By.CLASS_NAME, "promocode").send_keys("rahulshettyacademy")
    driver.find_element(By.CLASS_NAME, "promoBtn").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

    actual_discount = driver.find_element(By.CLASS_NAME, "discountPerc").text
    expected_discount = '10%'

    status.append(actual_discount == expected_discount)

    displayCase("Test Case 4: Check if the discount is applied with correct percentage", status[3])

    expected_price_to_pay = round((float(expected_sum) - (10 / 100) * expected_sum), 1)
    actual_price_to_pay = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)

    status.append(actual_price_to_pay == expected_price_to_pay)

    displayCase("Test Case 5: Check the calculation of discount amount", status[4])

    print("Hence Test Scenario is ", scenarioStatus(status))

    driver.close()
