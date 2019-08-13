from selenium import webdriver  # 使用的是selenium库中的webdiver，一种自动控制浏览器的第三方库
from selenium.webdriver.common.action_chains import ActionChains  # 对浏览器元素操作的库
import time  # 程序执行时间方面的控制


def spider_two_year(url):
    '''

    :param url: 要爬取的城市对应的网页
    :return: Time_list: 该城市两年不同时间对应的房价。时间序列对应房价的列表，列表中的每个数据类型为字典
            x_y: 对应的纵坐标信息（房价）构成的列表
    '''

    # 这一小块可以直接复制
    browser = webdriver.Chrome()  # 创建一个webdriver实例，是Chrome类型，browser可以看成是代表着目前网页的html
    browser.get(url)  # 通过网址跳转网页到url
    browser.maximize_window()  # 窗口最大化

    browser.implicitly_wait(5)  # 隐式等待，最多等5s
    js = "var q=document.documentElement.scrollTop=800"  # 800是设置的滚动距离
    browser.execute_script(js)  # js操作，向下活动页面，类似于滚轮

    time.sleep(1)  # 睡1s

    browser.implicitly_wait(5)  # 隐式等待，最多等5s
    # 找按钮，这里由于有两个按钮，为了保证不会找错，采取了几步进行，注意每一步的方法和返回值
    button = browser.find_element_by_class_name('trend_content').find_element_by_class_name('chartTools').find_elements_by_tag_name('li')[3]
    a = button.find_element_by_tag_name('a')
    a.click()  # click()点击操作

    browser.implicitly_wait(5)  # 隐式等待，最多等5s
    js = "var q=document.documentElement.scrollTop=800"  # 800是设置的滚动距离
    browser.execute_script(js)  # js操作，向下活动页面，类似于滚轮

    p = browser.find_element_by_class_name('highcharts-tracker')  # class_name， element
    Action = ActionChains(browser)  # 创建一个ActionChains对象，叫Action（import ActionChains库方法看最上面）
    Action.move_to_element(p).perform()  # 调用该第三方库方法，move_to_element(p)，将鼠标移到元素p上，perform()必须要加上，perform告诉程序执行此ActionChains方法
    time.sleep(2)  # 睡2s

    Action.move_by_offset(-586.5, 0).perform()  # 注意这里的move_by_offset()，这是在目前的鼠标位置进行移动，移动到的位置要注意一下，之后的for循环于之有关
    '''x坐标为正数向右偏移，x坐标为负数向左偏移'''
    '''y坐标为正数向下偏移，y坐标为负数向上偏移'''
    time.sleep(2)  # 睡2s

    time_list = []  # 创建空列表

    browser.implicitly_wait(5)  # 隐5s
    one = browser.find_element_by_class_name('highcharts-container')  # class_name，element
    browser.implicitly_wait(5)  # 隐5s
    two = one.find_element_by_tag_name('svg')  # tag_name， element
    browser.implicitly_wait(5)  # 隐5s
    three = two.find_elements_by_tag_name('g')[6]  # tag_name， elements，列表索引[6]
    browser.implicitly_wait(5)  # 隐5s
    four = three.find_element_by_tag_name('text')  # tag_name， element
    browser.implicitly_wait(5)  # 隐5s
    five = four.find_elements_by_tag_name('tspan')  # tag_name， element

    tm = {}  # 创建空字典
    name = five[1].text + five[0].text  # 对于有些节点，节点之间包含有文本信息的，可以用.text来获取其文本
    tm[name] = int(five[2].text)  # 字典的赋值方式，其中name就是键，int(five[2].text)就是值，保存到字典中就是 name:int(five[2].text)这样的类型
    time_list.append(tm)  # append()，列表添加元素的方法，将字典作为单个元素加进去

    for i in range(106):  # 循环次数比实际数据多，原因是距离有点难控制，所以比实际距离要小一些，为了把数据爬全，所以距离设小，次数设多
        Action.move_by_offset(11.5, 0).perform()  # 每次从当前位置向右移动11.5的距离（窗口的距离）
        time.sleep(1)  # 睡1s

        # 与上面相同
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

    # 最后一次移动，距离实在太难设置了
    Action.move_by_offset(10, 0).perform()  # 从当前位置向右移动10
    time.sleep(1)  # 睡1s

    # 与上面相同
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

    # 这一段是排除time_list中的重复项，由于距离比实际短，有些点会爬取两次，有两条数据
    Time_list = []  # 创建空列表
    for i in time_list:  # 循环遍历列表
        if i not in Time_list:  # if语句，not in用于判断i对应的元素是否存在于Time_list中，不在为True
            Time_list.append(i)  # append()列表添加元素方法

    # 获取图像纵坐标信息
    x_y = []  # 空列表
    X = browser.find_elements_by_class_name('highcharts-axis')[1].find_elements_by_tag_name('text')[:-1]  # 注意查找方法和返回值，最后有一个切片，左闭右开
    for x in X:  # 遍历循环列表
        w = x.find_element_by_tag_name('tspan')  # tag_name
        x_y.append(int(w.text[:-1]))  # append()，int()，w.text，[:-1]，共四个知识点

    time.sleep(2)
    browser.quit()
    return Time_list, x_y


# 测试
# url = 'http://sh.fangjia.com/gujia'
# Time_list, x_y = spider_two_year(url)  # 调用函数，爬取两年的信息
# print(Time_list)
# print(x_y)