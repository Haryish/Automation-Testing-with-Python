import time

import pytest
from selenium import webdriver
# from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        serviceObj = Service()  # selenium webservice Manager / seleniumManager
        driver = webdriver.Chrome(service=serviceObj)

    baseURL = 'https://rahulshettyacademy.com/angularpractice/'
    driver.maximize_window()
    driver.get(baseURL)
    request.cls.driver = driver
    yield
    driver.close()
