*** Settings ***
Resource          ../../../main_resources.robot

*** Variables ***

${url}    http://www.tatacliq.com/
${searchtext}    iphone

*** Keywords ***
Close_Browser_Session
    close_browser_all_windows

