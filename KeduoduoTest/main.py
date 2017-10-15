# -*- coding: utf-8 -*-
from common.log_utils import convert_to_json, export_logs, export_dict_to_json
import mainpage_test
import orders_center_test
from selenium import webdriver
from login_test import LoginPage
from mainpage_test import MainPage


if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path='/Users/SeaMonster/Downloads/chromedriver')
    print(browser.get_window_size())
    browser.maximize_window()
    # o1 = mainpage_test.shop_analysis(browser)
    # o2 = mainpage_test.sell_analysis(browser)
    # export_dict_to_json(o1._asdict(), '店铺经营分析.json')
    # export_dict_to_json(o2._asdict(),'营销效果分析.json')
    # orders_center_test.order_query_test(browser)

    login = LoginPage(browser)
    login.execute()
    main_page = MainPage(browser)
    main_page.execute()


    browser.quit()