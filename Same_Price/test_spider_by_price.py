from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


def spider_price_house(KEYWORD, price_1, price_2):
    browser = webdriver.Chrome()
    url = 'https://bj.5i5j.com/'
    browser.get(url)
    browser.maximize_window()

    where = browser.find_element_by_class_name('icon-city')
    where.click()
    City = []
    city = browser.find_elements_by_class_name('city')
    for t in city:
        c = t.find_element_by_tag_name('a')
        City.append(c.text)

    print(City)

    ershoufang = browser.find_element_by_class_name('top-nav').find_element_by_tag_name('li').find_element_by_tag_name('a')
    ershoufang.click()  # 点击了二手房
    browser.close()

    browser.switch_to_window(browser.window_handles[-1])  # 切换到最后一个窗口
    time.sleep(2)
    browser.implicitly_wait(10)
    input_1 = browser.find_element_by_id('priceLow')
    browser.implicitly_wait(10)
    input_2 = browser.find_element_by_id('priceTop')
    browser.implicitly_wait(10)
    input_1.send_keys(price_1)
    browser.implicitly_wait(10)
    input_2.send_keys(price_2)

    browser.implicitly_wait(10)
    button = browser.find_elements_by_class_name('btnQ')
    print(button)
    button[0].click()

    browser.switch_to_window(browser.window_handles[-1])  # 切换到最后一个窗口
    time.sleep(2)
    browser.implicitly_wait(10)

    # 此方法可以爬取详细信息（没写完，数量太多，操作慢）
    # House = browser.find_elements_by_class_name('listImg')
    # for i in House:
    #     i.click()
    #     browser.switch_to_window(browser.window_handles[-1])  # 切换到最后一个窗口
    #     browser.close()

    h = browser.find_element_by_class_name('pList')
    li = h.find_elements_by_tag_name('li')

    House_list = []
    for l in li:
        picture = l.find_element_by_class_name('listImg')
        house_href =picture.find_element_by_tag_name('a').get_attribute('href')
        picture_href = picture.find_element_by_tag_name('a').find_element_by_tag_name('img').get_attribute('src')
        information = l.find_element_by_class_name('listCon')
        inf_1 = information.find_element_by_class_name('listTit')
        inf_2 = information.find_element_by_class_name('listX')
        inf_3 = information.find_element_by_class_name('listTag')

        title = inf_1.find_element_by_tag_name('a').text
        p = inf_2.find_elements_by_tag_name('p')
        div = inf_2.find_element_by_tag_name('div')

        house_inf = p[0].text
        house_position = p[1].find_element_by_tag_name('a').text
        distance_subway = p[1].text[3:]
        people = p[2].text
        price = div.find_elements_by_tag_name('p')
        house_price = price[0].find_element_by_tag_name('strong').text
        one_price = price[1].text
        others_inf = inf_3.find_elements_by_tag_name('span')

        others = ''
        for i in others_inf:
            others = others + i.text + '，'

        house = {}
        house['房子链接'] = house_href
        house['图片链接'] = picture_href
        house['标题'] = title
        house['户型'] = house_inf.split('·')[0]
        house['建面'] = house_inf.split('·')[1]
        house['朝向'] = house_inf.split('·')[2]
        house['楼层'] = house_inf.split('·')[3]
        house['装修'] = house_inf.split('·')[4]
        house['小区'] = house_position
        house['其他位置信息'] = distance_subway
        house['关注人数'] = people.split('·')[0]
        house['带看次数'] = people.split('·')[1]
        house['发布时间'] = people.split('·')[2]
        house['总价'] = house_price
        house['单价'] = one_price[2:]
        house['其他信息'] = others
        House_list.append(house)

    print(House_list)
    return House_list

# 测试
if __name__ == '__main__':
    spider_price_house('长沙', 100, 200)
