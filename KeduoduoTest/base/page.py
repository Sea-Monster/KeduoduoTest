# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from KeduoduoTest.common.settings import IMAGE_PATH, LOGS_PATH, IMAGE_SUBFIX_DEFAULT, BASE_URL, BASE_LOGIN_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from common import file_utils, log_utils
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    """
    用于所有页面的继承
    """
    LOGIN_URL = BASE_LOGIN_URL + 'login.jsp'
    SELL_LIST_URL = BASE_LOGIN_URL + 'tbSellerList.jsp'
    MAIN_PAGE = BASE_URL + 'kdd/home.jsp'
    # 隐式等待秒数
    WAIT_SECONDS = 10
    # 点击前鼠标悬停秒数
    HOLD_SECONDS = 1

    def __init__(self, browser=None, catalog=None):
        """
        初始化，接收browser
        :type browser: WebDriver
        :param browser: 
        """
        self._browser = browser

        if self._browser is not None:
            self._browser.implicitly_wait(self.WAIT_SECONDS)

        if callable is None:
            self._catalog = '未分类'
        else:
            self._catalog = catalog

    @property
    def browser(self):
        if self._browser is None:
            self._browser = webdriver.Chrome(executable_path='/Users/SeaMonster/Downloads/chromedriver')
        br: WebDriver = self._browser
        return br

    def find_element(self, by=By.ID, value=None, browser=None):
        """

        :param by:
        :param value:
        :param browser:
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        return br.find_element(by, value)

    def save_screenshot(self, filename=None, browser=None):
        """
        保存截图
        到目录： /Users/SeaMonster/PycharmProjects/KeduoduoTest/images/{日期}/
        :param filename:
        :param browser:
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        now = datetime.datetime.now()
        file_path = IMAGE_PATH + str(now.date()) + '/' + self._catalog
        file_name = '' if filename is None else filename
        # 创建路径
        file_utils.make_directory(file_path)
        file_name = file_path + '/' + file_name + '_' + str(now) + IMAGE_SUBFIX_DEFAULT
        print('file name:' + file_name)
        return br.save_screenshot(file_name)

    def execute_script(self, script, *args, browser=None):
        """
        执行JavaScript代码
        :param script:
        :param args:
        :param browser:
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        try:
            return br.execute_script(script, *args)
        except Exception as e:
            log_utils.error(e)
            raise e

    def switch_to_frame(self, frame_reference, browser=None):
        """
        切换irame
        :param frame_reference:
        :param browser:
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        return br.switch_to.frame(frame_reference)

    def switch_to_default_content(self, browser=None):
        """
        切换到上一级iFrame
        :param browser: F
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        return br.switch_to.default_content()

    def find_element_by_css_selector(self, css_selector, browser=None, throw=False):
        """

        :param throw: 是否向上抛出异常
        :param css_selector:
        :param browser:
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        try:
            return br.find_element_by_css_selector(css_selector)
        except Exception as e:
            log_utils.error('find element by css fail : {0}'.format(css_selector))
            log_utils.error(e)
            if throw:
                raise e

    def find_elements_by_css_selector(self, css_selector, browser=None, throw=False):
        """

        :param throw: 是否向上抛出异常
        :param css_selector:
        :param browser:
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        try:
            return br.find_elements_by_css_selector(css_selector)
        except Exception as e:
            log_utils.error('find elements by css fail : {0}'.format(css_selector))
            log_utils.error(e)
            if throw:
                raise e

    def click(self, element, need_hold=False, browser=None):
        """
        点击
        :type element: WebElement
        :param element: 元素
        :param need_hold: 是否需要先"悬停"
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        if need_hold:
            ActionChains(br).move_to_element(element).perform()
            self.wait(self.HOLD_SECONDS)
        element.click()

    def click_by_css_selector(self, css_selector, need_hold=False, browser=None):
        """
        点击
        :param css_selector:
        :param need_hold:
        :param browser:
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        element = self.find_element_by_css_selector(css_selector, br)
        if need_hold:
            ActionChains(br).move_to_element(element).perform()
            self.wait(self.HOLD_SECONDS)
        element.click()

    def execute(self, browser=None):
        """
        执行特定操作(由子类决定步骤)
        :param browser:
        :return:
        """
        raise NotImplemented

    def wait_until(self, timeout=5, poll_frequency=0.5, locator_by=By.ID, locator_text='', browser=None):
        """
        显式等待
        :param timeout:
        :param poll_frequency:
        :param locator_by:
        :param locator_text:
        :param browser:
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        element: WebElement = WebDriverWait(br, timeout, poll_frequency).until(
            EC.presence_of_element_located((locator_by, locator_text))
        )
        return element

    def get(self, relative_url, browser=None):
        """
        Get 指定相对网址
        :param relative_url:
        :param browser:
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        return br.get(BASE_URL + relative_url)

    def get_absolute(self, url, browser=None):
        """
        Get 指定绝对网址
        :param url:
        :param browser:
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        return br.get(url)

    def open_new_tab(self, url=None, browser=None):
        """
        打开新标签页
        :param url:
        :param browser:
        :return: 旧的标签页，新打开的标签页
        """
        if url is None:
            return
        br: WebDriver = browser if browser is not None else self.browser
        old_handle = self._browser.current_window_handle
        old_handles = [item for item in self._browser.window_handles]
        self.execute_script('window.open("{0}")'.format(BASE_URL + url))
        new_handles = [item for item in self._browser.window_handles]
        new_handle = None
        for item in new_handles:
            if item in old_handles:
                pass
            else:
                new_handle = item
        br.switch_to.window(new_handle)
        ActionChains(br).send_keys(Keys.COMMAND, 't')
        return old_handle, new_handle
        # ActionChains(br).key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()

    def close_new_tab(self, handles, browser=None):
        """
        关闭新打开的标签页
        :param handles: 旧的标签页， 新的标签页（要关闭的那个）
        :param browser:
        :return:
        """
        br: WebDriver = browser if browser is not None else self.browser
        br.switch_to.window(handles[1])
        br.close()
        br.switch_to.window(handles[0])

    @classmethod
    def wait(cls, sec):
        """
        休眠
        :param sec: 休眠的秒数
        :return:
        """
        time.sleep(sec)

    def _set_browser(self, browser):
        br: WebDriver = browser if browser is not None else self.browser
        if self.browser is None:
            self._browser = br


if __name__ == '__main__':
    # a = datetime.datetime.now().date()
    # b = datetime.datetime.strptime(str(a), '%Y-%m-%d')
    # print(str(a))
    # print(b)
    pass
