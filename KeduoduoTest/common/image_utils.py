# -*- coding: utf-8 -*-
from .settings import LOGS_PATH, IMAGE_PATH
from selenium.webdriver.remote.webdriver import WebDriver

def screen_shoot(browser, filename, filepath=IMAGE_PATH):
    """

    :type browser: WebDriver
    """
    browser.save_screenshot(filepath + filename)
