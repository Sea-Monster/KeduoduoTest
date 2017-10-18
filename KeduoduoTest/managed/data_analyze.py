# -*- coding: utf-8 -*-
# 订单量，买家量， 订单金额分析

from KeduoduoTest.base.page import BasePage
from KeduoduoTest.common import log_utils




class AbstractAnalyze(BasePage):
    """
    订单量分析，买家量分析，订单金额分析很相似
    """
    _url = 'kdd/main.jsp?menu=customer&id=ddfx'

    _locate_css = {
        '时间从': '#contrast_frist',
        '时间到': '#contrast_last',
        '状态': 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(5) > div > table div',
        '状态-等待出库': 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(5) > div > div > table > tbody > tr:nth-child(1) > td > label > input[type="checkbox"]',
        '状态-等待确认收货': 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(5) > div > div > table > tbody > tr:nth-child(2) > td > label > input[type="checkbox"]',
        '状态-完成': 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(5) > div > div > table > tbody > tr:nth-child(3) > td > label > input[type="checkbox"]',
        '状态-确认收货': 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(5) > div > div > table > tbody > tr:nth-child(4) > td > label > input[type="checkbox"]',
        '状态-未付款': 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(5) > div > div > table > tbody > tr:nth-child(5) > td > label > input[type="checkbox"]',
        '状态-已付款': 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(5) > div > div > table > tbody > tr:nth-child(6) > td > label > input[type="checkbox"]',
        '查询': 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(6) > button',
        '当天': 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(7) > button',
        '昨天': 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(8) > button',
        '本周': 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(9) > button',
        '本月': 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(10) > button'
    }

    def __init__(self, browser=None, catalog=None):
        super().__init__(browser, catalog)

    def execute(self, browser=None):
        self.get(self._url)
        status_list = '状态-完成', '状态-确认收货', '状态-未付款'

        self._select_time_from('2017-09-01')
        self._select_time_to('2017-10-31')
        self._select_status(status_list)
        self._query()
        self.wait(3)
        self.save_screenshot('特定条件')
        self.browser.refresh()

        self._query_today()
        self.wait(3)
        self.save_screenshot('今天')
        self._query_yesterday()
        self.wait(3)
        self.save_screenshot('昨天')
        self._query_week()
        self.wait(3)
        self.save_screenshot('本周')
        self._query_month()
        self.wait(3)
        self.save_screenshot('本月')

    def _select_time_from(self, time_from=None):
        """
        设定时间（从）
        :param time_from:   yyyy-MM-dd格式的日期字符串
        :return:
        """
        time = time_from if time_from is not None else ''
        time_id = self._locate_css.get('时间从').split('#')[1]
        self.execute_script('document.getElementById("{0}").value="{1}";'.format(time_id, time))

    def _select_time_to(self, time_to=None):
        """
        设定时间（到）
        :param time_to: yyyy-MM-dd格式的日期字符串
        :return:
        """
        time = time_to if time_to is not None else ''
        time_id = self._locate_css.get('时间到').split('#')[1]
        self.execute_script('document.getElementById("{0}").value="{1}";'.format(time_id, time))

    def _select_status(self, status_list=None):
        """

        :param status_list:
        :return:
        """
        # 先点状态才能选状态
        self.click_by_css_selector(self._locate_css.get('状态'), need_hold=True)
        # 已付款是默认的，所以先取消掉
        self.click_by_css_selector(self._locate_css.get('状态-已付款'), need_hold=True)
        if status_list is not None:
            check_list = status_list[:3]
            for status in check_list:
                locate = self._locate_css.get(status)
                if locate is not None:
                    self.click_by_css_selector(locate, need_hold=True)


    def _query(self):
        """
        点击查询按钮
        :return:
        """
        self.click_by_css_selector(self._locate_css.get('查询'))

    def _query_today(self):
        """
        查询当天
        :return:
        """
        self.click_by_css_selector(self._locate_css.get('当天'))

    def _query_yesterday(self):
        """
        查询昨天
        :return:
        """
        self.click_by_css_selector(self._locate_css.get('昨天'))

    def _query_week(self):
        """
        查询本周
        :return:
        """
        self.click_by_css_selector(self._locate_css.get('本周'))

    def _query_month(self):
        """
        查询当月
        :return:
        """
        self.click_by_css_selector(self._locate_css.get('本月'))


class OrderAnalyze(AbstractAnalyze):
    """
    订单量分析
    """
    _url = 'kdd/operate_center.jsp?str=dingdan'

    def __init__(self, browser=None, catalog='经营中心/订单量分析'):
        super().__init__(browser, catalog)


class BuyerAnalyze(AbstractAnalyze):
    """
    买家量分析
    """
    _url = 'kdd/operate_center.jsp?str=mjl'

    def __init__(self, browser=None, catalog='经营中心/买家量分析'):
        super().__init__(browser, catalog)


class OrderMoneyAnalyze(AbstractAnalyze):
    """
    订单金额分析
    """
    _url = 'kdd/operate_center.jsp?str=ddje'

    def __init__(self, browser=None, catalog='经营中心/订单金额分析'):
        super().__init__(browser, catalog)
        self._locate_css['状态-已付款'] = 'body > div:nth-child(1) > div.searchCondition > table > tbody > tr > td:nth-child(5) > div > div > table > tbody > tr:nth-child(5) > td > label > input[type="checkbox"]'
        self._locate_css['状态-未付款'] = None



if __name__ == '__main__':
    from KeduoduoTest.login_test import LoginPage
    from KeduoduoTest.common.webdriver_utils import get_web_driver

    browser = get_web_driver()
    login = LoginPage(browser)
    login.execute()

    a1 = OrderAnalyze(browser)
    a1.execute()
    a2 = BuyerAnalyze(browser)
    a2.execute()
    a3 = OrderMoneyAnalyze(browser)
    a3.execute()
