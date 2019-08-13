from selenium import webdriver  # 使用的是selenium库中的webdiver，一种自动控制浏览器的第三方库
from selenium.webdriver.common.action_chains import ActionChains  # 对浏览器元素操作的库


# 爬取网站上有的城市信息
def spider_place_allow():
    '''

    :return: 网站上具有的城市及其对应的url构成的字典
    '''

    browser = webdriver.Chrome()  # 创建一个webdriver实例，是Chrome类型，browser可以看成是代表着目前网页的html
    url = 'http://bj.fangjia.com/zoushi'
    browser.get(url)  # 通过网址跳转网页到url

    # 使display变成block，如果不是block是不能爬取的
    button = browser.find_element_by_id('selectedCity')  # by_id，通过id属性查找

    # 注意：调用ActionChains库的时候，不要再窗口上移动鼠标（这个库操作的是chromedriver的虚拟鼠标，如果在窗口上移动鼠标会取代其控制，导致数据无法爬取）
    Action = ActionChains(browser)  # 创建一个ActionChains对象，叫Action（import ActionChains库方法看最上面）
    Action.move_to_element(button).perform()  # 调用该第三方库方法，move_to_element(p)，将鼠标移到元素p上，perform()必须要加上，perform告诉程序执行此ActionChains方法

    others = browser.find_element_by_id('moreCity')  # by_id，通过id属性查找
    city = others.find_elements_by_tag_name('div')  # by_tag_name，按节点名找，elements，返回列表

    number = browser.find_element_by_class_name('wzhi')  # by_class_name，按class属性查找
    letter = number.find_elements_by_tag_name('li')  # by_tag_name，按节点名找，elements，返回列表

    city_dic = {}  # 创建空字典
    for i in range(len(letter)):  # range()，len()
        Action.move_to_element(letter[i]).perform()  # letter[i]， move_to_element移动到letter[i]对应的节点，perform()执行
        the_city = city[i].find_elements_by_tag_name('a')  # by_tag_name，按节点名找，elements，返回列表
        for ct in the_city:
            city_dic[ct.text] = ct.get_attribute('href')
            # 注意：这里分两部分，第一部分是字典的赋值方法，其中ct.text就是键，ct.get_attribute('href')就是值，保存到字典中就是 ct.text:ct.get_attribute('href')这样的类型
            # ct.text获取ct对应节点的文本信息，ct.get_attribute('href')获取ct对应节点的href信息，这里要使用get_attribute()方法

    browser.quit()  # 关闭所有用程序打开的窗口
    return city_dic


# 测试
if __name__ == '__main__':
    city_dic = spider_place_allow()
    print(city_dic)
