# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# driver.get_screenshot_as_file("testbaidu.png")
# cook = driver.get_cookies()
# print(cook)
title = driver.title
html = driver.page_source
print(title)
driver.quit()