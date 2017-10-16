# -*- coding: utf-8 -*-
import sys
import os

# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from common.log_utils import convert_to_json, export_logs, export_dict_to_json
import mainpage_test
import orders_center_test
from selenium import webdriver
from login_test import LoginPage
from mainpage_test import MainPage

if __name__ == '__main__':

    if len(sys.argv)>1 and sys.argv[1] == 'nopic':
        chrome_opt = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_opt.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(executable_path='/Users/SeaMonster/Downloads/chromedriver',
                                   chrome_options=chrome_opt)
    else:
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
