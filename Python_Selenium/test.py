#coding:utf-8
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#selenium
#http://code.google.com/p/selenium/


#Drive for Chrome
#http://chromedriver.storage.googleapis.com/index.html?path=2.9/
#http://code.google.com/p/selenium/wiki/ChromeDriver

#Example
#http://rfyiamcool.blog.51cto.com/1030776/1309512


#browser = webdriver.Firefox()
#browser = webdriver.IE()
browser = webdriver.Chrome()

browser.get('http://www.yahoo.com')
assert 'Yahoo!' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()