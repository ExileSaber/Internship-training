from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


# 爬取一年的房价信息
def spider_one_year(url):
    '''

    :param url: 要爬取的城市对应的网页
    :return: 该城市一年不同时间对应的房价
    '''
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    browser.implicitly_wait(10)
    span = browser.find_element_by_class_name('highcharts-series')
    print(span)

    js = "var q=document.documentElement.scrollTop=900"
    browser.execute_script(js)

    time.sleep(5)
    browser.implicitly_wait(5)
    points = span.find_elements_by_tag_name('path')[4:]

    Time_list = []

    for p in points:
        Action = ActionChains(browser)
        Action.move_to_element(p).perform()
        time.sleep(1)
        browser.implicitly_wait(5)
        one = browser.find_element_by_class_name('highcharts-container')
        browser.implicitly_wait(5)
        two = one.find_element_by_tag_name('svg')
        browser.implicitly_wait(5)
        three = two.find_elements_by_tag_name('g')[6]
        browser.implicitly_wait(5)
        four = three.find_element_by_tag_name('text')
        browser.implicitly_wait(5)
        five = four.find_elements_by_tag_name('tspan')

        tm = {}
        name = five[1].text + five[0].text
        tm[name] = int(five[2].text)
        Time_list.append(tm)

    browser.close()
    return Time_list