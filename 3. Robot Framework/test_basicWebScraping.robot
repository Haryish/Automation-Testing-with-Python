*** Settings ***
Library    SeleniumLibrary
Library    XML
Documentation    Basic Web Scrapping using Robot framework
Test Teardown    Close Browser
Resource         page_actions.robot

*** Variables ***
${DemoQA_MENU}       Forms
${DemoQA_SUBMENU}    Practice Form
${load_time}    5
${loginpage_username}    rahulshettyacademy
${loginpage_password}    learning

*** Test Cases ***
# Group 1: Positive scenarios
Test if we can initialize browser and render to url
    Open AutomationPractice
    Check if the title matches the same

Test that we can able to login using text fields
    Open LoginpagePractise
    Enter the text on username field
    Enter the password field
    Provide other inputs
    Submit the form
    Check if the page navigates to ProtoCommerce page

Evaluate if we can able to fill the form using Automation
    Open DemoQAcom
    Navigate to web form section
    Enter the form details
    Submit the DemoQAcom form


*** Keywords ***
# Test Case 1
Check if the title matches the same
    Maximize Browser Window
    Sleep    ${load_time}
    Title Should Be    Practice Page

# Test Case 2
Enter the text on username field
    Input Text    //input[@id='username']    ${loginpage_username} 

Enter the password field
    Input Password    css:#password    ${loginpage_password}

Provide other inputs
    Select Radio Button    radio    user
    Wait Until Element Is Visible    //button[@id='okayBtn']
    Click Button    //button[@id='okayBtn']
    # Alert Should Be Present
    # Handle Alert    action=Okay
    Select Checkbox    //input[@type="checkbox" and @name="terms"]

Submit the form
    Click Button    css:#signInBtn
    # Wait Until Element Contains  //input[@id='signInBtn']    Signing In...
    ${updated_value}=    SeleniumLibrary.Get Element Attribute    css:#signInBtn    value
    Should Be Equal    ${updated_value}    Signing ..
    Sleep    ${load_time}
    

Check if the page navigates to ProtoCommerce page
    Title Should Be    ProtoCommerce

# Test Case 3
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



