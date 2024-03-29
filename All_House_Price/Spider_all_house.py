from selenium import webdriver
import time


def spider_all_house(url, place, number):
    if number % 30 == 0:
        num = int(number/30)
    else:
        num = int(number/30) + 1

    browser = webdriver.Chrome()  # 构建一个Chrome浏览器对象
    browser.get(url)  # 加载网页
    browser.maximize_window()  # 最大化

    browser.implicitly_wait(10)  # 隐式等待，10s内未加载出来则报错
    ershoufang = browser.find_element_by_class_name('top-nav').find_element_by_tag_name('li').find_element_by_tag_name('a')  # 查找节点方式
    ershoufang.click()  # 点击了二手房
    browser.close()  # 关闭目前打开的窗口

    browser.switch_to_window(browser.window_handles[-1])  # 切换到最后一个窗口
    time.sleep(2)  # 程序睡眠2s
    browser.implicitly_wait(10)
    first = browser.find_element_by_class_name('new_di_tab')
    places = first.find_elements_by_tag_name('a')[1:]

    Places = {}  # 字典
    for p in places:
        li = p.find_element_by_tag_name('li')
        Places[li.text] = li

    Places[place].click()  # 点击操作
    time.sleep(5)

    House_list = []  # 列表
    flag = 0
    for i in range(num):
        browser.implicitly_wait(10)
        h = browser.find_element_by_class_name('pList')
        li = h.find_elements_by_tag_name('li')

        f = 0
        for l in li:
            f += 1
            if len(li) != 30:
                if f in [16, 17, 18, 19]:  # 用来判断，除去广告部分
                    pass
                else:
                    # 各种相应的信息
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
            else:
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
    browser.quit()  # 退出browser对象
    return House_list


# 测试
# spider_all_house('https://bj.5i5j.com/', '朝阳', 100)