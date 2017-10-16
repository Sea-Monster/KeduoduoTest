# -*- coding: utf-8 -*-
# 订单中心

from base.page import BasePage
from common import log_utils


class OrderCenterPage(BasePage):
    """
    订单中心（订单查询）
    """
    _order_center_url = 'http://14.119.106.43:8300/kdd/main.jsp?menu=order&id=ddcx'
    #_order_center_url = 'http://14.119.106.43:8300/kdd/order_center.jsp?str=allOrder'

    _frame_id = 'main'

    # --------  操作位置 -----------------
    # 今日订单
    # _locate_today_order_id = 'settTitle'
    _locate_today_order = '#settTitle>ul>li:nth-child(2)>a'
    # 每页条数
    _locate_page_rows = '#pageRows'
    _locate_page_rows_500 = _locate_page_rows + '>option:nth-child(5)'
    # 订单数
    _locate_total_count = '#totalCount'
    _locate_order_detail_frame = '.cboxIframe'

    # --------  操作位置 结束--------------

    def __init__(self, browser=None, catalog='订单中心'):
        super(OrderCenterPage, self).__init__(browser, catalog)

    def execute(self, browser=None):
        self.browser.get(self._order_center_url)
        # 切换到右侧的主iFrame
        self.switch_to_frame(self._frame_id)
        self._query_order_today()

    def _query_order_today(self, browser=None):
        """
        查询今天订单
        :param browser:
        :return:
        """
        if browser is None:
            browser = self.browser
        ele = self.find_element_by_css_selector(self._locate_today_order, throw=True)
        # self.click(ele)
        totalCount_element = self.find_element_by_css_selector(self._locate_total_count)
        # 如果成功查到数据
        if totalCount_element and totalCount_element.text != '':
            log_utils.info('今日订单数：' + totalCount_element.text)
            # 每页条数设为500条
            ele = self.find_element_by_css_selector(self._locate_page_rows_500)
            self.click(ele)
            # 遍历订单记录
            locate_view_detail = '#tab2 tr:nth-child({0})>td:nth-child(12)>a'
            for i in range(2, 502):
                try:
                    ele = self.find_element_by_css_selector(locate_view_detail.format(str(i)), throw=True)
                    self.click(ele, need_hold=True)
                    self._show_order_detail()
                    self.wait(1)
                except:
                    break

    def _show_order_detail(self, browser=None):
        """
        订单详情
        :param browser:
        :return:
        """
        # 关闭按钮
        locate_close = '#cboxClose'

        iFrame = self.find_element_by_css_selector(self._locate_order_detail_frame)
        self.switch_to_frame(iFrame)
        js = 'document.getElementsByClassName("cboxIframe")[0].scrollTop=300'
        self.execute_script(js)

        self.switch_to_default_content()
        iFrame = self.find_element_by_css_selector(self._frame_id)
        self.switch_to_frame(iFrame)

        # 关闭
        ele = self.find_element_by_css_selector(locate_close)
        self.click(ele, need_hold=True)


if __name__ == '__main__':
    from selenium import webdriver
    from login_test import LoginPage

    chrome_opt = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_opt.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(executable_path='/Users/SeaMonster/Downloads/chromedriver',
                               chrome_options=chrome_opt)
    login = LoginPage(browser)
    login.execute()
    order = OrderCenterPage(browser)
    order.execute()
