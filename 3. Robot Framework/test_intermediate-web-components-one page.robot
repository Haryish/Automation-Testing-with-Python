*** Settings ***
Library    SeleniumLibrary
Library    XML
Documentation    Basic Web Scrapping using Robot framework
Test Setup       Open DemoQAcom
Test Teardown    Close Browser
Resource         page_actions.robot

*** Variables ***
${DemoQA_MENU}       Forms
${DemoQA_SUBMENU}    Practice Form
${load_time}    5
${loginpage_username}    rahulshettyacademy
${loginpage_password}    learning

*** Test Cases ***
Count the number of menus and submenus in DemoQA page
    Navigate to any elements
    Get the element counts on DemoQA page
    Get the list of menus and set to menus
    Get the count subelement on each menus
    Get the list of submenus and set to menus correspondingly
    Log the menus and submenus

Evaluate if we can able to work with @{DemoQA_SUBMENU} under @{DemoQA_MENU}
    Navigate to @{DemoQA_SUBMENU} under @{DemoQA_MENU}
    Fill the relevant inputs and submit
    Check if the details appeared on submittion

Evaluate if we can able to work with @{DemoQA_SUBMENU} under @{DemoQA_MENU}
    Navigate to @{DemoQA_SUBMENU} under @{DemoQA_MENU}
    Check the parent folder
    Uncheck the parent folder
    Check any child page


Evaluate if we can able to work with @{DemoQA_SUBMENU} under @{DemoQA_MENU}
Evaluate if we can able to work with @{DemoQA_SUBMENU} under @{DemoQA_MENU}
Evaluate if we can able to work with @{DemoQA_SUBMENU} under @{DemoQA_MENU}
Evaluate if we can able to work with @{DemoQA_SUBMENU} under @{DemoQA_MENU}
Evaluate if we can able to work with @{DemoQA_SUBMENU} under @{DemoQA_MENU}
Evaluate if we can able to work with @{DemoQA_SUBMENU} under @{DemoQA_MENU}
Evaluate if we can able to work with @{DemoQA_SUBMENU} under @{DemoQA_MENU}

    

Evaluate if we can able to fill the form using Automation
    Open DemoQAcom
    Navigate to web form section
    Enter the form details
    Submit the DemoQAcom form


*** Keywords ***
Navigate to web form section
    Click Element    (//div[normalize-space()='Forms'])[1]
    Sleep    ${load_time}
    Click Element    //div[.//div[contains(text(),'${DemoQA_MENU}')]]//ul/li/*[contains(text(),'${DemoQA_SUBMENU}')]

Enter the form details
    ${TITLE_HEADER}=    Get Text    //h1[contains(text(),'Practice Form')]
    Should Be Equal    ${TITLE_HEADER}    Practice Form


Submit the DemoQAcom form
    Execute Javascript    window.scrollTo(0, document.body.scrollHeight)
    Click Button    //button[@id='submit']
