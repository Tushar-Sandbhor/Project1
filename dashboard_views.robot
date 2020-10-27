*** Settings ***
Force Tags   DashBoardView
Resource      dashboard_views_resource.robot
#Suite Teardown    Close_Browser_Session

*** Test Cases ***

assignment2
    [Tags]   Sitelogin
    [Documentation]
    logintosite   ${url}
    filterdata   ${searchtext}
    ${data}   getlabel  
    getproductinfo  ${data}[2]
    		