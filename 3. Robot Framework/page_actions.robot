*** Settings ***
Library    SeleniumLibrary


*** Keywords ***
Open AutomationPractice
    Open Browser    https://rahulshettyacademy.com/AutomationPractice/    chrome

Open LoginpagePractise
    Open Browser    https://rahulshettyacademy.com/loginpagePractise/    chrome

Open DemoQAcom
    Open Browser    https://demoqa.com/    chrome


# Available menus
# //div[@class='element-group']//div[contains(text(),'Elements')]

# Inspect group of elements
# //div[.//div[contains(text(),'Elements')]]//ul/li

# Inspect individual menu based on element group
# //div[.//div[contains(text(),'Elements')]]//ul/li/*[contains(text(),'Check Box')]
