import time
import Spider_place_allow
import Spider_two_year
# import Spider_one_year
import Write_in_mongoDB
import Draw_line_chart


print('搜集初始数据,leading.......')
time.sleep(2)

city_list = Spider_place_allow.spider_place_allow()
keywords = list(city_list.keys())
print("搜集完成")
keyword = input("输入要查询的省份：")

if keyword in keywords:
    url = city_list[keyword]
    # time_list = Spider_one_year.spider_one_year(url)  # 调用函数，爬取一年的信息
    Time_list, x_y = Spider_two_year.spider_two_year(url)  # 调用函数，爬取两年的信息
    print(Time_list)

    save = input("是否存入数据库：")
    if save == '是':
        Write_in_mongoDB.write_in_mongoDB(Time_list, keyword)
    else:
        print('End')

    draw = input("是否绘制图像：")
    if draw == '是':
        Draw_line_chart.draw_line_chart(Time_list, keyword)
    else:
        print('End')

else:
    print('房价网中没有你要查询的城市信息，只能选取链家网进行查询')




