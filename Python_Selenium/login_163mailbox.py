#coding:utf-8
import sys

from selenium import webdriver
url = "http://mail.163.com"

driver = webdriver.Chrome()
driver.get(url)

#type the username
element = driver.find_element_by_id("idInput")
element.send_keys('')
element = driver.find_element_by_id("pwdInput")
element.send_keys('')

element = driver.find_element_by_id("loginBtn")
#element = driver.find_element_by_link_text('登陆')
element.click()

element = driver.find_element_by_id("_mail_component_2_2")
element.click()
#type the password
#element.submit()

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")
backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart
print "WebPage: %s" % url
print " Back End: %s" % backendPerformance
print " Front End: %s" % frontendPerformance
#driver.quit()