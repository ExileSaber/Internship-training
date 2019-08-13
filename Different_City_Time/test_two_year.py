from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
url = 'http://sh.fangjia.com/zoushi'
browser.get(url)
browser.maximize_window()

browser.implicitly_wait(5)
js = "var q=document.documentElement.scrollTop=800"
browser.execute_script(js)

time.sleep(1)

browser.implicitly_wait(5)
button = browser.find_element_by_class_name('trend_content').find_element_by_class_name('chartTools').find_elements_by_tag_name('li')[3]
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
tm[name] = five[2].text
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
    tm[name] = five[2].text
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
tm[name] = five[2].text
time_list.append(tm)

Time_list = []
for i in time_list:
    if i not in Time_list:
        Time_list.append(i)

print(Time_list)
print(len(Time_list))
