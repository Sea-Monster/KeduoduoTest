# -*- coding: utf-8 -*-
from selenium import webdriver
from KeduoduoTest.common import settings


def get_web_driver():
    if settings.NO_PIC:
        chrome_opt = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_opt.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(executable_path='/Users/SeaMonster/Downloads/chromedriver',
                                   chrome_options=chrome_opt)
        return browser
    else:
        browser = webdriver.Chrome(executable_path='/Users/SeaMonster/Downloads/chromedriver')
        return browser
