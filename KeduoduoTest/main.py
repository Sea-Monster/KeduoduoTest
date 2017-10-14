# -*- coding: utf-8 -*-
from common.login_utils import login_keduoduo
import mainpage_test
from selenium import webdriver


if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path='/Users/SeaMonster/Downloads/chromedriver')
    login_keduoduo(browser)