from selene import browser

browser.open("https://demowebshop.tricentis.com/")

browser.element('.ico-login').click()
browser.element('#Email').type('yashaka@gmail.com')
browser.element('#Password').type('Pa$$word')
browser.element('.login-button').click()