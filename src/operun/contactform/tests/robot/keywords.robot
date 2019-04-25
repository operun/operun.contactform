*** Keywords ***

# SITE

I'm logged in as a '${ROLE}'
    Enable autologin as  ${ROLE}

I am logged in as site administrator
    Element should be visible  css=body.userrole-site-administrator

# ACTIONS

Fill text field
    [arguments]  ${field_label}   ${text}
    Input Text  xpath=//form//div/input[preceding-sibling::label[contains(text(), '${field_label}')]]  ${text}

I navigate to the site login
    Go To  ${PLONE_URL}/login_form
    Wait Until Element Is Visible  xpath=(//form[@id="login_form"])

I enter valid credentials
    Input Text  __ac_name  admin
    Input Text  __ac_password  secret
    Click Element  //input[@name="submit"]

I am logged in
    Wait until page contains  Sie sind nun angemeldet
    Page should contain  Sie sind nun angemeldet
