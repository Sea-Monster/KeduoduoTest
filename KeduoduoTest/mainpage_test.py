# -*- coding: utf-8 -*-
# 首页的测试
# 店铺经营分析区
# 当天
# 昨天
# 本周
# 本月
# 营销效果分析区
# 最近一次
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
from base.page import BasePage


class MainPage(BasePage):
    """
    首页的测试
    """
    _ShopData = collections.namedtuple('ShopData', ['销售总额', '订单总量', '买家总数', '待付款订单量', '待出库订单量', '商品销售总量'])
    _ShopDatas = collections.namedtuple('ShopDatas', ['当天', '昨天', '本周', '本月'])
    _SellData = collections.namedtuple('SellData', ['营销号码数', '链接点击率', '营销拍单率',
                                                    '营销成交率', '营销成交总额', 'ROI',
                                                    '意向客户率'])
    _SellDatas = collections.namedtuple('SellDatas', ['最近一次', '当天', '本周', '本月'])

    def __init__(self, browser=None, catalog='首页'):
        self.Fuck = ''
        super().__init__(browser, catalog)

    def execute(self, browser=None):
        super()._set_browser(browser)
        self.browser.get(self.MAIN_PAGE)
        self.wait(3)
        self._shop_analysis()

    def _shop_analysis(self, browser=None):
        """
        店铺经营分析区
        :param browser:
        :return:
        """
        if browser is None:
            browser = self.browser

        # 当天
        shop_today = self._ShopData(*self._get_attrs(browser))

        # 昨天
        browser.find_element_by_css_selector(
            'body>div.content>div.wrapperLeft>div.leftD1>div.dataTitle>ul>li:nth-child(3)> a').click()

        shop_yesterday = self._ShopData(*self._get_attrs(browser))

        # 本周
        browser.find_element_by_css_selector(
            'body>div.content>div.wrapperLeft>div.leftD1>div.dataTitle>ul>li:nth-child(4)> a').click()
        shop_week = self._ShopData(*self._get_attrs(browser))

        # 本月
        browser.find_element_by_css_selector(
            'body>div.content>div.wrapperLeft>div.leftD1>div.dataTitle>ul>li:nth-child(5)> a').click()
        shop_month = self._ShopData(*self._get_attrs(browser))

        shop_datas = self._ShopDatas(shop_today._asdict(), shop_yesterday._asdict(), shop_week._asdict(),
                                     shop_month._asdict())

        print(shop_datas)
        return shop_datas

    def _sell_analysis(self, browser=None):
        """
        营销效果分析区
        :type browser: WebDriver
        :param browser:
        :return:
        """
        # 最近一次
        sell_last = self._SellData(*self._get_yxs(browser))
        # 当天
        browser.find_element_by_css_selector(
            'body>div.content>div.wrapperLeft>div.leftD2>div.dataTitle>ul>li:nth-child(3)>a').click()
        sell_today = self._SellData(*self._get_yxs(browser))
        # 本周
        browser.find_element_by_css_selector(
            'body>div.content>div.wrapperLeft>div.leftD2>div.dataTitle>ul>li:nth-child(4)>a').click()
        sell_week = self._SellData(*self._get_yxs(browser))
        # 本月
        browser.find_element_by_css_selector(
            'body>div.content>div.wrapperLeft>div.leftD2>div.dataTitle>ul>li:nth-child(5)>a').click()
        sell_month = self._SellData(*self._get_yxs(browser))

        sell_datas = self._SellDatas(sell_last._asdict(), sell_today._asdict(), sell_week._asdict(),
                                     sell_month._asdict())
        print(sell_datas)
        # browser.save_screenshot(settings.IMAGE_PATH + '1.png')

        return sell_datas

    def _data_analysis(self, browser=None):
        """

        :return:
        """
        pass

    def _get_attrs(self, browser):
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

    def _get_yxs(self, browser):
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
