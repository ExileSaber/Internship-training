import Spider_city_allow
import time
import Write_in_mongoDB
import Spider_place
import Spider_all_house

print('搜集初始数据,leading.......')
time.sleep(2)

url = 'https://bj.5i5j.com/'  # 进入的初始网址
City = Spider_city_allow.spider_city_allow(url)
print(City)

print("搜集完成")
city = input("输入你要查询的城市：")

keys = list(City.keys())

if city in keys:
    url_city = City[city]
    Places = Spider_place.spider_place(url_city)

    print(city + "可查询的区域有：", Places)
    place = input("输入你要查询的区域：")
    if place in Places:
        number = int(input("输入你需要查看的房子数量:"))
        House_list = Spider_all_house.spider_all_house(url_city, place, number)

    else:
        print("没有该区域")

    save = input("是否存入数据库：")
    if save == '是':
        Write_in_mongoDB.write_in_mongoDB(House_list, city, place)

else:
    print("你输入的城市我爱我家网中没有，暂无其他网站可以进行操作")
