from selenium import webdriver  # 使用的是selenium库中的webdiver，一种自动控制浏览器的第三方库
from selenium.webdriver.common.action_chains import ActionChains  # 对浏览器元素操作的库
import time  # 程序执行时间方面的控制


# 爬取一年的房价信息
def spider_one_year(url):
    '''

    :param url: 要爬取的城市对应的网页
    :return: 该城市一年不同时间对应的房价的列表。时间序列对应房价的列表，列表中的每个数据类型为字典
    '''

    # 这一小块可以直接复制
    browser = webdriver.Chrome()  # 创建一个webdriver实例，是Chrome类型，browser可以看成是代表着目前网页的html
    browser.get(url)  # 通过网址跳转网页到url
    browser.maximize_window()  # 窗口最大化

    browser.implicitly_wait(10)  # 隐式等待，最多等10s
    span = browser.find_element_by_class_name('highcharts-series')
    # 注意查询方法，首先是browser.···是在网页中找相关的节点信息
    # 其次find_element_by_class_name()有两个要注意的地方，一个是find_···，后面是element，只找一个，如果是elements，找多个
    # 另外是by_····后面是class_name，是用class属性来查找（class属性值是可以重复的，要注意冲突）
    print(span)  # 输出看一下

    # 这一小块可以直接复制
    js = "var q=document.documentElement.scrollTop=900"  # 900是设置的滚动距离
    browser.execute_script(js)  # js操作，向下活动页面，类似于滚轮

    time.sleep(5)  # time库的方法，让程序睡眠5秒，好可以下实现了什么功能
    browser.implicitly_wait(5)  # 隐式等待，最多等5s
    points = span.find_elements_by_tag_name('path')[4:]  # 切片
    # 注意查询方法，首先是browser.···是在网页中找相关的节点信息
    # 其次find_element_by_class_name()有两个要注意的地方，一个是find_···，后面是elements，找多个，返回的是列表
    # 另外是by_····后面是tag_name，是用节点名来查找（常用于一个节点没有class属性，id属性）

    Time_list = []  # 创建一个空列表
    for p in points:  # 循环遍历points列表中的元素，每次p从points中获取一个元素，开始执行后面内容，之后再获取下一个，再执行，直到最后
        # 注意：调用ActionChains库的时候，不要再窗口上移动鼠标（这个库操作的是chromedriver的虚拟鼠标，如果在窗口上移动鼠标会取代其控制，导致数据无法爬取）
        Action = ActionChains(browser)  # 创建一个ActionChains对象，叫Action（import ActionChains库方法看最上面）
        Action.move_to_element(p).perform()  # 调用该第三方库方法，move_to_element(p)，将鼠标移到元素p上，perform()必须要加上，perform告诉程序执行此ActionChains方法
        time.sleep(1)  # 睡1s
        browser.implicitly_wait(5)  # 隐5s
        one = browser.find_element_by_class_name('highcharts-container')
        # 注意查询方法，首先是browser.···是在网页中找相关的节点信息
        # 其次find_element_by_class_name()有两个要注意的地方，一个是find_···，后面是element，只找一个，如果是elements，找多个
        # 另外是by_····后面是class_name，是用class属性来查找（class属性值是可以重复的，要注意冲突）

        browser.implicitly_wait(5)  # 隐5s
        two = one.find_element_by_tag_name('svg')  # by_tag_name，按节点名找，element
        browser.implicitly_wait(5)
        three = two.find_elements_by_tag_name('g')[6]  # elements，返回列表
        browser.implicitly_wait(5)
        four = three.find_element_by_tag_name('text')  # element
        browser.implicitly_wait(5)
        five = four.find_elements_by_tag_name('tspan')  # elements，返回列表

        tm = {}  # 创建空字典
        name = five[1].text + five[0].text  # 对于有些节点，节点之间包含有文本信息的，可以用.text来获取其文本
        tm[name] = int(five[2].text)  # 字典的赋值方式，其中name就是键，int(five[2].text)就是值，保存到字典中就是 name:int(five[2].text)这样的类型
        Time_list.append(tm)  # append()，列表添加元素的方法，将字典作为单个元素加进去

    browser.quit()  # 关闭所有用程序打开的窗口
    return Time_list


# 测试
# url = 'http://sh.fangjia.com/gujia'
# Time_list = spider_one_year(url)
# print(Time_list)