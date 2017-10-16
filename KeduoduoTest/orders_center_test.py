# -*- coding: utf-8 -*-
# 订单中心

from base.page import BasePage
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.image_utils import screen_shoot
from selenium.webdriver.common.action_chains import ActionChains

def order_query_test(browser):
    """

    :type browser: WebDriver
    """
    order_center_url = 'http://14.119.106.43:8300/kdd/main.jsp?menu=order&id=ddcx'
    browser.get(order_center_url)
    _order_today_query_test(browser)


def _order_today_query_test(browser):
    """

    :type browser: WebDriver
    """
    # 点击今日订单
    browser.switch_to.frame('main')
    WebDriverWait(browser, 10, 0.5).until(
        EC.presence_of_element_located((By.ID, 'settTitle'))
    )

    # time.sleep(1)
    browser.find_element_by_css_selector('#settTitle>ul>li:nth-child(2)>a').click()
    # browser.execute_script("window.parent.order_day('order_center.jsp?str=TodayTheOrder','所有订单,order_center.jsp?str=allOrder,今日订单,order_center.jsp?str=TodayTheOrder');")
    time.sleep(3)
    # WebDriverWait(browser, 5, 0.5).until(
    #     EC.presence_of_element_located((By.ID, 'totalCount'))
    # )
    totalCount_element = browser.find_element_by_css_selector('#totalCount')
    totalCount = int(totalCount_element.text) if totalCount_element.text!='' else 0
    print('今日订单数：' + str(totalCount))

    for i in range(2, 502):
        try:
            click_element = browser.find_element_by_css_selector(
            '#tab2 tr:nth-child({0})>td:nth-child(12)>a'.format(str(i)))
            ActionChains(browser).move_to_element(click_element).perform()  # 先悬停
            time.sleep(1)
            click_element.click()
            _order_detail_test(browser)
            time.sleep(1)
        except Exception as e:
            print(e)
            break


def _order_detail_test(browser):
    """
    订单详情
    :param browser:
    :return:
    """
    time.sleep(1)
    iframe = browser.find_element_by_css_selector('.cboxIframe')
    browser.switch_to_frame(iframe)
    order_id = browser.find_element_by_css_selector('body>.wrapBox>.colorbox_rcon>.rconc>div:nth-child(2) table tr:nth-child(1)>td:nth-child(2)').text
    screen_shoot(browser, filename='订单' + order_id + 'A.png')

    js = "document.documentElement.scrollTop=800"
    browser.execute_script(js)

    screen_shoot(browser, filename='订单' + order_id + 'B.png')

    browser.switch_to.default_content()
    iframe = browser.find_element_by_css_selector('#main')
    browser.switch_to.frame(iframe)

    close_element = browser.find_element_by_css_selector('#cboxClose')
    ActionChains(browser).move_to_element(close_element).perform()
    time.sleep(3)
    close_element.click()


class OrderCenterPage(BasePage):
    """
    订单中心
    """
    _order_center_url = 'http://14.119.106.43:8300/kdd/main.jsp?menu=order&id=ddcx'

    def __init__(self, browser=None, catalog='订单中心'):
        super().__init__(browser, catalog)

    def execute(self, browser=None):
        return super().execute(browser)


