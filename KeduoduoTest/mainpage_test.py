# -*- coding: utf-8 -*-
# 首页的测试
    # 店铺经营分析区
        # 当天
        # 昨天
        # 本周
        # 本月
    # 营销效果分析区
        #最近一次
        # 当天
        # 本周
        # 本月
    # 数据趋势分析区
        # 当天
        # 昨天
        # 本周
        # 本月
    # 客服

    # 通道情况

#

import collections
from selenium.webdriver.remote.webdriver import WebDriver
from common import settings
import json
import time




_shop_attr_list = ['销售总额', '订单总量', '买家总数', '待付款订单量', '待出库订单量', '商品销售总量']
_shop_day_list = ['当天', '昨天', '本周', '本月']
ShopData = collections.namedtuple('ShopData', _shop_attr_list)
ShopDatas = collections.namedtuple('ShopDatas', _shop_day_list)
SellData = collections.namedtuple('SellData', ['营销号码数','链接点击率', '营销拍单率',
                                               '营销成交率', '营销成交总额', 'ROI',
                                               '意向客户率'])
SellDatas = collections.namedtuple('SellDatas', ['最近一次','当天','本周','本月'])

_main_page = 'http://14.119.106.43:8300/kdd/home.jsp'

def shop_analysis(browser):
    """
    店铺经营分析区
    :type browser: WebDriver
    :return:
    """
    browser.get(_main_page)
    time.sleep(3)

    # 当天
    shop_today = ShopData(*_get_attrs(browser))

    # 昨天
    browser.find_element_by_css_selector(
        'body>div.content>div.wrapperLeft>div.leftD1>div.dataTitle>ul>li:nth-child(3)> a').click()

    shop_yesterday = ShopData(*_get_attrs(browser))

    # 本周
    browser.find_element_by_css_selector(
        'body>div.content>div.wrapperLeft>div.leftD1>div.dataTitle>ul>li:nth-child(4)> a').click()
    shop_week = ShopData(*_get_attrs(browser))

    # 本月
    browser.find_element_by_css_selector(
        'body>div.content>div.wrapperLeft>div.leftD1>div.dataTitle>ul>li:nth-child(5)> a').click()
    shop_month = ShopData(*_get_attrs(browser))

    shop_datas = ShopDatas(shop_today._asdict(), shop_yesterday._asdict(), shop_week._asdict(), shop_month._asdict())

    print(shop_datas)
    return shop_datas



def sell_analysis(browser):
    """
    营销效果分析区
    :type browser: WebDriver
    :return:
    """
    # 最近一次
    sell_last = SellData(*_get_yxs(browser))
    # 当天
    browser.find_element_by_css_selector(
        'body>div.content>div.wrapperLeft>div.leftD2>div.dataTitle>ul>li:nth-child(3)>a').click()
    sell_today = SellData(*_get_yxs(browser))
    # 本周
    browser.find_element_by_css_selector(
        'body>div.content>div.wrapperLeft>div.leftD2>div.dataTitle>ul>li:nth-child(4)>a').click()
    sell_week = SellData(*_get_yxs(browser))
    # 本月
    browser.find_element_by_css_selector(
        'body>div.content>div.wrapperLeft>div.leftD2>div.dataTitle>ul>li:nth-child(5)>a').click()
    sell_month = SellData(*_get_yxs(browser))

    sell_datas = SellDatas(sell_last._asdict(), sell_today._asdict(), sell_week._asdict(), sell_month._asdict())
    print(sell_datas)
    # browser.save_screenshot(settings.IMAGE_PATH + '1.png')

    return sell_datas


def data_analysis():
    pass


def _get_attrs(browser):
    """
    获取店铺经营分析区的数据
    :param browser:
    :return:
    """
    list1 = list()
    for i in range(1, 7):
        d = browser.find_element_by_css_selector('#val' + str(i)).text
        list1.append(d)
    return list1


def _get_yxs(browser):
    """
    获取营销效果分析区的数据
    :param browser:
    :return:
    """
    list1 = list()
    for i in range(1, 8):
        d = browser.find_element_by_css_selector('#yxVal' + str(i)).text
        list1.append(d)
    return list1






