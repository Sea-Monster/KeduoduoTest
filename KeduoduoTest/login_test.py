# -*- coding: utf-8 -*-
from base.page import BasePage
from selenium.webdriver.common.by import By
from common import settings


class LoginPage(BasePage):
    """
    登录页
    """

    def __init__(self, browser=None, catalog='登录页'):
        """
        初始化
        :param browser:
        :param catalog:
        """
        super().__init__(browser, catalog)

    def execute(self, browser=None):
        """
        执行登录操作
        :param browser:
        :return:
        """
        super()._set_browser(browser)

        self.browser.get(self.LOGIN_URL)
        element_username = self.wait_until(timeout=5, poll_frequency=0.5, locator_text='username')
        element_username.clear()
        element_username.send_keys(settings.USER_NAME)
        element_pwd = self.find_element_by_css_selector('#password')
        element_pwd.clear()
        element_pwd.send_keys(settings.PASSWORD)

        login_btn = self.find_element_by_css_selector('#iframe_box>div>div>div.singbtn>input')
        login_btn.click()

        self.wait_until(5, 0.5, By.PARTIAL_LINK_TEXT, '注销')
        self.browser.get(self.SELL_LIST_URL)

        self.wait_until(locator_text='totalCount')

        self.execute_script("toLogin('爱斯贝绮')")
