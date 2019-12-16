from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://erp.ncuindia.edu')

usernameStr = 'your username'
passwordStr = 'your password'


username = browser.find_element_by_id('tbUserName')
username.send_keys(usernameStr)


password = browser.find_element_by_id('tbPassword')
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('btnLogIn')
signInButton.click()

attendance = browser.find_element_by_id('aAttandance')
attendance.click()