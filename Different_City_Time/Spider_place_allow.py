from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def spider_place_allow():
    try:
        browser = webdriver.Chrome()
        url = 'http://bj.fangjia.com/zoushi'
        browser.get(url)

        # 使display变成block
        button = browser.find_element_by_id('selectedCity')
        Action = ActionChains(browser)
        Action.move_to_element(button).perform()

        others = browser.find_element_by_id('moreCity')
        city = others.find_elements_by_tag_name('div')

        number = browser.find_element_by_class_name('wzhi')
        letter = number.find_elements_by_tag_name('li')

        city_list = {}
        # flag = 0  # 测试
        for i in range(len(letter)):
            Action.move_to_element(letter[i]).perform()
            the_city = city[i].find_elements_by_tag_name('a')
            for ct in the_city:
                city_list[ct.text] = ct.get_attribute('href')
                # flag = flag + 1

    finally:
        browser.quit()
        # print(city_list)
        return city_list


# 测试
if __name__ == '__main__':
    spider_place_allow()
