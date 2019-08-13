from selenium import webdriver
import time


def spider_by_price(url, price_1, price_2, number):
    if number % 30 == 0:
        num = int(number/30)
    else:
        num = int(number/30) + 1

    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    ershoufang = browser.find_element_by_class_name('top-nav').find_element_by_tag_name('li').find_element_by_tag_name('a')
    ershoufang.click()  # 点击了二手房
    browser.close()

    browser.switch_to_window(browser.window_handles[-1])  # 切换到最后一个窗口
    time.sleep(2)
    browser.implicitly_wait(10)
    button = browser.find_elements_by_class_name('btnQ')

    browser.implicitly_wait(10)
    input_1 = browser.find_element_by_id('priceLow')
    browser.implicitly_wait(10)
    input_2 = browser.find_element_by_id('priceTop')
    browser.implicitly_wait(10)
    input_1.send_keys(price_1)
    browser.implicitly_wait(10)
    input_2.send_keys(price_2)

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

    House_list = []
    flag = 0
    for i in range(num):
        h = browser.find_element_by_class_name('pList')
        li = h.find_elements_by_tag_name('li')

        for l in li:
            browser.implicitly_wait(10)

            picture = l.find_element_by_class_name('listImg')
            house_href = picture.find_element_by_tag_name('a').get_attribute('href')
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
            house['总价'] = house_price + '万'
            house['单价'] = one_price[2:]
            house['其他信息'] = others
            House_list.append(house)

            flag = flag + 1
            if flag == number:
                break

        if flag == number:
            break

        time.sleep(2)
        xiayiye = browser.find_element_by_class_name('cPage')
        xiayiye.click()

    print(House_list)
    print(len(House_list))
    browser.quit()
    return House_list
