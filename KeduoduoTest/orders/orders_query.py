# -*- coding: utf-8 -*-
# 订单查询
from base.page import BasePage
from common import log_utils

criteria_locate_css = {
    '买家账号': '#pin',
    '买家姓名': '#fullName1',
    '订单编号': '',
    '电话': '',
    '省份': '',
    '买家备注': '',
    '卖家备注': '',
    '商品名称': '',
    '购买次数从': '',
    '购买次数至': '',
    '订单状态': '',
    '实付金额从': '',
    '实付金额至': '',
    '下单时间从': '',
    '下单时间至': '',
    '排序方式': '',
    '排序次序': ''
}


class OrdersQueryPage(BasePage):
    """
    订单查询页
    """
    _order_detail_url = 'kdd/order_detail.jsp?orderId={0}'
    # --------  操作位置 -----------------
    # 每页条数
    _locate_page_rows = '#pageRows'
    _locate_page_rows_500 = _locate_page_rows + '>option:nth-child(5)'
    # 订单数
    _locate_total_count = '#totalCount'
    _locate_order_detail_frame = '.cboxIframe'

    # --------  操作位置 结束--------------

    def __init__(self, browser=None, catalog='订单中心/订单查询'):
        super().__init__(browser, catalog)

    def _query_default(self, show_detail=0, browser=None):
        """
        今日订单的默认查询
        :param show_detail: 显示（头）多少条明细记录
        :param browser:
        :return:
        """
        if browser is None:
            browser = self.browser
        total_count_element = self.find_element_by_css_selector(self._locate_total_count)
        self.wait(1)
        # 如果成功查到数据
        if total_count_element and total_count_element.text != '':
            log_utils.info('今日订单数：' + total_count_element.text)
            # 每页条数设为500条
            ele = self.find_element_by_css_selector(self._locate_page_rows_500)
            self.click(ele)

            # 截图
            self.wait(2)
            self.execute_script('document.documentElement.scrollTop=0')
            self.wait(1)
            self.save_screenshot('订单默认查询')

            # 遍历订单记录
            locate_order_id = '#tab2 tr:nth-child({0})>td:nth-child(8)'

            if show_detail > 0:
                for i in range(2, 502):
                    try:
                        if show_detail < i - 1:
                            break
                        element_order_id = self.find_element_by_css_selector(locate_order_id.format(str(i)))
                        order_id = element_order_id.text
                        self._show_order_detail(order_id)
                        self.wait(1)
                    except Exception as e:
                        log_utils.error(e)
                        break
        else:
            log_utils.error('无法获取订单总数')
            log_utils.error(total_count_element)
            log_utils.error(total_count_element.text)

    def _show_order_detail(self, order_id=None, browser=None):
        """
        订单详情
        :param browser:
        :return:
        """
        if order_id is None:
            return

        # 新标签页
        handles = self.open_new_tab(self._order_detail_url.format(str(order_id)))
        self.wait(2)

        self.save_screenshot('订单详情' + str(order_id))

        self.wait(1)

        # 关闭当前标签页
        self.close_new_tab(handles)


class OrdersAllPage(OrdersQueryPage):
    """
    所有订单
    """
    _url = 'kdd/order_center.jsp?str=allOrder'

    def __init__(self, browser=None, catalog='订单中心/订单查询/所有订单'):
        super().__init__(browser, catalog)

    def execute(self, browser=None):
        super()._set_browser(browser)
        self.get(self._url)
        self._query_default(show_detail=3)


class OrdersTodayPage(OrdersQueryPage):
    """
    今日订单
    """
    _url = 'kdd/order_center.jsp?str=TodayTheOrder'

    def __init__(self, browser=None, catalog='订单中心/订单查询/今日订单'):
        super().__init__(browser, catalog)

    def execute(self, browser=None):
        super()._set_browser(browser)
        self.get(self._url)
        self._query_default()


if __name__ == '__main__':
    from KeduoduoTest.login_test import LoginPage
    from KeduoduoTest.common.webdriver_utils import get_web_driver

    browser = get_web_driver()
    login = LoginPage(browser)
    login.execute()

    log_utils.info('------- 测试今日订单 -------------')
    order_today = OrdersTodayPage(browser)
    order_today.execute()

    log_utils.info('------- 测试所有订单 -------------')
    order_all = OrdersAllPage(browser)
    order_all.execute()
