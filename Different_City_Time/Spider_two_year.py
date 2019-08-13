from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


def spider_two_year(url):
    '''

    :param url: 要爬取的城市对应的网页
    :return: 该城市两年不同时间对应的房价
    '''
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    browser.implicitly_wait(5)
    js = "var q=document.documentElement.scrollTop=800"
    browser.execute_script(js)

    time.sleep(1)

    browser.implicitly_wait(5)
    button = browser.find_element_by_class_name('trend_content').find_element_by_class_name(
        'chartTools').find_elements_by_tag_name('li')[3]
    a = button.find_element_by_tag_name('a')
    a.click()

    browser.implicitly_wait(5)
    js = "var q=document.documentElement.scrollTop=800"
    browser.execute_script(js)

    p = browser.find_element_by_class_name('highcharts-tracker')
    Action = ActionChains(browser)
    Action.move_to_element(p).perform()
    time.sleep(2)

    Action.move_by_offset(-586.5, 0).perform()
    time.sleep(2)

    time_list = []

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
    time_list.append(tm)

    for i in range(106):
        Action.move_by_offset(11.5, 0).perform()
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
        time_list.append(tm)

    Action.move_by_offset(10, 0).perform()
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
    time_list.append(tm)

    Time_list = []
    for i in time_list:
        if i not in Time_list:
            Time_list.append(i)

    # 获取图像纵坐标信息
    x_y = []
    X = browser.find_elements_by_class_name('highcharts-axis')[1].find_elements_by_tag_name('text')[:-1]
    for x in X:
        w = x.find_element_by_tag_name('tspan')
        x_y.append(int(w.text[:-1]))

    time.sleep(2)
    browser.close()
    return Time_list, x_y
