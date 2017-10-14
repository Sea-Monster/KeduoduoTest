# -*- coding: utf-8 -*-

from selenium import webdriver
import time

login_url = 'http://14.119.106.43:8250/login.jsp'
main_url = 'http://14.119.106.43:8300/kdd/home.jsp'
sell_list_url = 'http://14.119.106.43:8250/tbSellerList.jsp'

browser = webdriver.Chrome(executable_path='/Users/SeaMonster/Downloads/chromedriver')
browser.get('http://14.119.106.43:8250/login.jsp')
time.sleep(3)

element_username = browser.find_element_by_id('username')
# print(element_username)
element_username.clear()
element_username.send_keys('stone')

element_pwd = browser.find_element_by_id('password')
element_pwd.clear()
element_pwd.send_keys('stone')

login_btn = browser.find_element_by_css_selector('#iframe_box>div>div>div.singbtn>input')
login_btn.click()

time.sleep(3)
browser.get(sell_list_url)
time.sleep(3)
browser.execute_script("toLogin('爱斯贝绮')")

#
# # 查询有效用户
# browser.find_element_by_css_selector('#distabled>option:nth-child(2)').click()
# browser.find_element_by_css_selector('#right>div>div.right_huifu_1>div:nth-child(2)>a:nth-child(1)').click()
# time.sleep(3)
# # 用 "爱斯贝绮" 登录
# browser.find_element_by_css_selector('#xl>tbody >tr:nth-child(2)>td:nth-child(2)>a:nth-child(2)').click()




# browser.quit()