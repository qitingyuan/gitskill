# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:03:46 2017

@author: sgd
"""


from selenium import webdriver
import time
'''driver = webdriver.Firefox()'''
driver = webdriver.Chrome()
driver.get("http://183.230.175.37:10000/museum_develop/web")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_name('username').send_keys('admin')
time.sleep(3)
driver.find_element_by_name('password').send_keys('admin')
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='login']/form/input[3]").click()