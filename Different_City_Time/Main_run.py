import time

# 下面全都是导入的自己写的py文件名，相当于第三方库
import Spider_place_allow
import Spider_two_year
# import Spider_one_year
import Write_in_mongoDB
import Draw_line_chart


print('搜集初始数据,leading.......')
time.sleep(2)

city_list = Spider_place_allow.spider_place_allow()  # 执行自己写的库中的函数
keywords = list(city_list.keys())  # 字典所有键信息转换成列表
print("搜集完成")
keyword = input("输入要查询的省份：")  # python的输入方法input()，中间的字符串会先输出再屏幕上，再通过键盘输入对应的值

if keyword in keywords:
    url = city_list[keyword]  # 这里就体现出了字典的好处，直接用键可以找到值
    # time_list = Spider_one_year.spider_one_year(url)  # 调用函数，爬取一年的信息
    Time_list, x_y = Spider_two_year.spider_two_year(url)  # 调用函数，爬取两年的信息
    print(Time_list)  # 输出看一下

    save = input("是否存入数据库：")  # python的输入方法input()，中间的字符串会先输出再屏幕上，再通过键盘输入对应的值
    if save == '是':
        Write_in_mongoDB.write_in_mongoDB(Time_list, keyword)  # 执行自己写的库中的函数
    else:
        print('End')

    draw = input("是否绘制图像：")  # python的输入方法input()，中间的字符串会先输出再屏幕上，再通过键盘输入对应的值
    if draw == '是':
        Draw_line_chart.draw_line_chart(Time_list, keyword)  # 执行自己写的库中的函数
    else:
        print('End')

else:
    print('房价网中没有你要查询的城市信息，只能选取链家网进行查询')




