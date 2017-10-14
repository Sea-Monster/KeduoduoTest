# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import time


def login_keduoduo(browser):
    """
    登录
    :type browser: WebDriver
    """
    LOGIN_URL = 'http://14.119.106.43:8250/login.jsp'
    SELL_LIST_URL = 'http://14.119.106.43:8250/tbSellerList.jsp'
    browser.get(LOGIN_URL)
    time.sleep(3)

    element_username = browser.find_element_by_id('username')
    element_username.clear()
    element_username.send_keys('stone')

    element_pwd = browser.find_element_by_id('password')
    element_pwd.clear()
    element_pwd.send_keys('stone')

    login_btn = browser.find_element_by_css_selector('#iframe_box>div>div>div.singbtn>input')
    login_btn.click()

    time.sleep(3)
    browser.get(SELL_LIST_URL)
    time.sleep(3)
    browser.execute_script("toLogin('爱斯贝绮')")

    return browser
