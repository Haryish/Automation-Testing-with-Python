***Settings***
Documentation   To verify stable opening of webapp
Library         SeleniumLibrary

*** Variables ***
${TITLE_EXPECTED}    LoginPage Practise | Rahul Shetty Academy

*** Test Cases ***
Validate the stability of web application
        open the url on the browser
        check if the webapp opens successfully

*** Keywords ***
open the url on the browser
    Create Webdriver    Chrome
    Go To    https://rahulshettyacademy.com/loginpagePractise/

check if the webapp opens successfully
    Maximize Browser Window
    Title Should Be    ${TITLE_EXPECTED}
    [Teardown]    Close Browser